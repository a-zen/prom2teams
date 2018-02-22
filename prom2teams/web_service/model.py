from flask_restplus import fields
from prom2teams.web_service.api import api

annotations = api.model('annotations', {
    'description': fields.String(default='disk usage 93% on rootfs device'),
    'summary': fields.String(default='Disk usage alert on CS30.evilcorp')
})

labels = api.model('labels', {
    'alertname': fields.String(default='DiskSpace'),
    'fstype': fields.String(default='rootfs'),
    'device': fields.String(default='rootfs'),
    'instance': fields.String(default='cs30.evilcorp'),
    'job': fields.String(default='fsociety'),
    'mounterpoint': fields.String(default='/'),
    'severity': fields.String(default='severe')
})

alert = api.model('alert', {
    'status': fields.String(default='Resolved'),
    'startsAt': fields.String(default='2017-05-09T07:01:37.803Z'),
    'endsAt': fields.String(default='2017-05-09T07:01:37.803Z'),
    'generatorURL': fields.String(default='my.prometheusserver.url'),
    'labels': fields.Nested(labels),
    'annotations': fields.Nested(annotations)
})

message = api.model('message', {
    'receiver': fields.String(default='test_webhook'),
    'status': fields.String(default='Resolved'),
    'alerts': fields.List(fields.Nested(alert)),
    'externalURL': fields.String(default='my.prometheusalertmanager.url'),
    'version': fields.String(default='4')
})