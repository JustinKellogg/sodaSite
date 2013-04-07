# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Machine'
        db.create_table(u'api_machine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('heatGood', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lastContact', self.gf('django.db.models.fields.DateTimeField')()),
            ('Admin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'api', ['Machine'])

        # Adding model 'InventorySlot'
        db.create_table(u'api_inventoryslot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sodaType', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Machine'])),
        ))
        db.send_create_signal(u'api', ['InventorySlot'])

        # Adding model 'Client'
        db.create_table(u'api_client', (
            ('auth_key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
        ))
        db.send_create_signal(u'api', ['Client'])

        # Adding model 'MachineUser'
        db.create_table(u'api_machineuser', (
            ('User', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], primary_key=True)),
            ('studentID', self.gf('django.db.models.fields.IntegerField')()),
            ('funds', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'api', ['MachineUser'])

        # Adding model 'Soda'
        db.create_table(u'api_soda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sugar', self.gf('django.db.models.fields.IntegerField')()),
            ('calories', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Slot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.InventorySlot'])),
            ('cost', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'api', ['Soda'])

        # Adding model 'Transaction'
        db.create_table(u'api_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('User', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.MachineUser'])),
        ))
        db.send_create_signal(u'api', ['Transaction'])

        # Adding model 'AdminTransaction'
        db.create_table(u'api_admintransaction', (
            (u'transaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['api.Transaction'], unique=True, primary_key=True)),
            ('Admin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'api', ['AdminTransaction'])

        # Adding model 'SodaTransaction'
        db.create_table(u'api_sodatransaction', (
            (u'transaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['api.Transaction'], unique=True, primary_key=True)),
            ('Soda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Soda'])),
        ))
        db.send_create_signal(u'api', ['SodaTransaction'])

        # Adding model 'Discount'
        db.create_table(u'api_discount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('Soda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Soda'])),
            ('offset', self.gf('django.db.models.fields.FloatField')()),
            ('startDate', self.gf('django.db.models.fields.DateTimeField')()),
            ('endDate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'api', ['Discount'])


    def backwards(self, orm):
        # Deleting model 'Machine'
        db.delete_table(u'api_machine')

        # Deleting model 'InventorySlot'
        db.delete_table(u'api_inventoryslot')

        # Deleting model 'Client'
        db.delete_table(u'api_client')

        # Deleting model 'MachineUser'
        db.delete_table(u'api_machineuser')

        # Deleting model 'Soda'
        db.delete_table(u'api_soda')

        # Deleting model 'Transaction'
        db.delete_table(u'api_transaction')

        # Deleting model 'AdminTransaction'
        db.delete_table(u'api_admintransaction')

        # Deleting model 'SodaTransaction'
        db.delete_table(u'api_sodatransaction')

        # Deleting model 'Discount'
        db.delete_table(u'api_discount')


    models = {
        u'api.admintransaction': {
            'Admin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'Meta': {'ordering': "['-date_time']", 'object_name': 'AdminTransaction', '_ormbases': [u'api.Transaction']},
            u'transaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['api.Transaction']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'api.client': {
            'Meta': {'object_name': 'Client'},
            'auth_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'})
        },
        u'api.discount': {
            'Meta': {'object_name': 'Discount'},
            'Soda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Soda']"}),
            'endDate': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'offset': ('django.db.models.fields.FloatField', [], {}),
            'startDate': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'api.inventoryslot': {
            'Machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Machine']"}),
            'Meta': {'object_name': 'InventorySlot'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sodaType': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'api.machine': {
            'Admin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'Meta': {'object_name': 'Machine'},
            'heatGood': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastContact': ('django.db.models.fields.DateTimeField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'api.machineuser': {
            'Meta': {'object_name': 'MachineUser'},
            'User': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'primary_key': 'True'}),
            'funds': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'studentID': ('django.db.models.fields.IntegerField', [], {})
        },
        u'api.soda': {
            'Meta': {'object_name': 'Soda'},
            'Slot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.InventorySlot']"}),
            'calories': ('django.db.models.fields.IntegerField', [], {}),
            'cost': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sugar': ('django.db.models.fields.IntegerField', [], {})
        },
        u'api.sodatransaction': {
            'Meta': {'ordering': "['-date_time']", 'object_name': 'SodaTransaction', '_ormbases': [u'api.Transaction']},
            'Soda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Soda']"}),
            u'transaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['api.Transaction']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'api.transaction': {
            'Meta': {'ordering': "['-date_time']", 'object_name': 'Transaction'},
            'User': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.MachineUser']"}),
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['api']