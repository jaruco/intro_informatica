#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Create or update admin user
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={'email': 'admin@example.com', 'is_staff': True, 'is_superuser': True}
)
admin_user.set_password('admin123')
admin_user.save()
print(f"{'✅ Created' if created else '✅ Updated'} admin user | Password: admin123")

# Create test user
test_user, created = User.objects.get_or_create(
    username='testuser',
    defaults={'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'User'}
)
test_user.set_password('testuser123')
test_user.save()
print(f"{'✅ Created' if created else '✅ Updated'} test user | Password: testuser123")

print("\n📝 Login Credentials:")
print("Admin: admin / admin123")
print("User:  testuser / testuser123")
