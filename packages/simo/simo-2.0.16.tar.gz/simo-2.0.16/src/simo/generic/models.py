import time
import sys
import traceback
from threading import Timer
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from simo.core.models import Instance, Component
from .controllers import AlarmGroup



@receiver(post_save, sender=Component)
def handle_alarm_groups(sender, instance, *args, **kwargs):
    if not instance.alarm_category:
        return
    if hasattr(instance, 'do_not_update_alarm_group'):
        return
    dirty_fields = instance.get_dirty_fields()
    if 'arm_status' not in dirty_fields:
        return

    for alarm_group in Component.objects.filter(
        controller_uid=AlarmGroup.uid,
        config__components__contains=instance.id,
    ).exclude(value='disarmed'):
        stats = {
            'disarmed': 0, 'pending-arm': 0, 'armed': 0, 'breached': 0
        }
        stats[instance.arm_status] += 1
        for slave in Component.objects.filter(
            pk__in=alarm_group.config['components'],
        ).exclude(pk=instance.pk):
            stats[slave.arm_status] += 1
        alarm_group.config['stats'] = stats
        alarm_group.save(update_fields=['config'])

        if stats['disarmed'] == len(alarm_group.config['components']):
            alarm_group_value = 'disarmed'
        elif stats['armed'] == len(alarm_group.config['components']):
            alarm_group_value = 'armed'
        elif stats['breached']:
            if alarm_group.value != 'breached':
                def notify_users_security_breach(alarm_group_component_id):
                    alarm_group_component = Component.objects.filter(
                        id=alarm_group_component_id, value='breached'
                    ).first()
                    if not alarm_group_component:
                        return
                    breached_components = Component.objects.filter(
                        pk__in=alarm_group_component.config['components'],
                        arm_status='breached'
                    )
                    body = "Security Breach! " + '; '.join(
                        [str(c) for c in breached_components]
                    )
                    from simo.notifications.utils import notify_users
                    notify_users(
                        alarm_group_component.zone.instance,
                        'alarm', str(alarm_group_component), body,
                        component=alarm_group_component
                    )
                if alarm_group.config.get('notify_on_breach') is not None:
                    t = Timer(
                        # give it one second to finish with other db processes.
                        alarm_group.config['notify_on_breach'] + 1,
                        notify_users_security_breach, [alarm_group.id]
                    )
                    t.start()
            alarm_group_value = 'breached'
        else:
            alarm_group_value = 'pending-arm'

        alarm_group.controller.set(alarm_group_value)


@receiver(pre_save, sender=Component)
def manage_alarm_groups(sender, instance, *args, **kwargs):
    if instance.controller_uid != AlarmGroup.uid:
        return

    if 'value' not in instance.get_dirty_fields():
        return

    if instance.value == 'breached':
        instance.meta['breach_start'] = time.time()
        instance.meta['events_triggered'] = []
    elif instance.get_dirty_fields()['value'] == 'breached' \
    and instance.value == 'disarmed':
        instance.meta['breach_start'] = None
        for event_uid in instance.meta.get('events_triggered', []):
            event = instance.controller.events_map.get(event_uid)
            if not event:
                continue
            if not event.get('disarm_action'):
                continue
            try:
                getattr(event['component'], event['disarm_action'])()
            except Exception:
                print(traceback.format_exc(), file=sys.stderr)


@receiver(post_delete, sender=Component)
def clear_alarm_group_config_on_component_delete(
    sender, instance, *args, **kwargs
):
    for ag in Component.objects.filter(
        base_type=AlarmGroup.base_type,
        config__components__contains=instance.id
    ):
        ag.config['components'] = [
            id for id in ag.config.get('components', []) if id != instance.id
        ]
        ag.save(update_fields=['config'])


@receiver(post_save, sender=Component)
def bind_controlling_locks_to_alarm_groups(sender, instance, *args, **kwargs):
    if instance.base_type != 'lock':
        return
    if 'value' not in instance.get_dirty_fields():
        return
    if instance.value == 'locked':
        for ag in Component.objects.filter(
            base_type=AlarmGroup.base_type,
            config__arming_locks__contains=instance.id
        ):
            ag.arm()
    elif instance.value == 'unlocked':
        for ag in Component.objects.filter(
            base_type=AlarmGroup.base_type,
            config__arming_locks__contains=instance.id
        ):
            ag.disarm()

