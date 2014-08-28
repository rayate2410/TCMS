# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestPlan'
        db.create_table(u'execution_testplan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('build', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Build'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('started_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'execution', ['TestPlan'])

        # Adding model 'ExecutionTask'
        db.create_table(u'execution_executiontask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testplan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['execution.TestPlan'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Category'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('allocated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='executiontask_allocated_by', to=orm['auth.User'])),
            ('allocated_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='executiontask_allocated_to', to=orm['auth.User'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('client_device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ClientDevice'])),
            ('browsers', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'execution', ['ExecutionTask'])

        # Adding model 'ExecutionHistory'
        db.create_table(u'execution_executionhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('execution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['execution.ExecutionTask'])),
            ('testcase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['testcase.TestCase'])),
            ('result', self.gf('django.db.models.fields.CharField')(default='NE', max_length=10)),
            ('bugid', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comment', self.gf('django.db.models.fields.TextField')(default='')),
            ('executed_by', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User'], null=True)),
            ('modified_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'execution', ['ExecutionHistory'])


    def backwards(self, orm):
        # Deleting model 'TestPlan'
        db.delete_table(u'execution_testplan')

        # Deleting model 'ExecutionTask'
        db.delete_table(u'execution_executiontask')

        # Deleting model 'ExecutionHistory'
        db.delete_table(u'execution_executionhistory')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'execution.executionhistory': {
            'Meta': {'object_name': 'ExecutionHistory'},
            'bugid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'executed_by': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['auth.User']", 'null': 'True'}),
            'execution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['execution.ExecutionTask']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'default': "'NE'", 'max_length': '10'}),
            'testcase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['testcase.TestCase']"})
        },
        u'execution.executiontask': {
            'Meta': {'object_name': 'ExecutionTask'},
            'allocated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'executiontask_allocated_by'", 'to': u"orm['auth.User']"}),
            'allocated_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'executiontask_allocated_to'", 'to': u"orm['auth.User']"}),
            'browsers': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Category']"}),
            'client_device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.ClientDevice']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'testplan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['execution.TestPlan']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'execution.testplan': {
            'Meta': {'object_name': 'TestPlan'},
            'build': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Build']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'started_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'project.build': {
            'Meta': {'object_name': 'Build'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'project.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"})
        },
        u'project.clientdevice': {
            'Meta': {'object_name': 'ClientDevice'},
            'client_device': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operating_system': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'testcase.testcase': {
            'Meta': {'object_name': 'TestCase'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Category']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expected_result': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_automated': ('django.db.models.fields.BooleanField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'steps': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['execution']