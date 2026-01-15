import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files import File
from learning_app.models import Badge

class Command(BaseCommand):
    help = 'Initialize badges with icons from a local directory'

    def handle(self, *args, **kwargs):
        # 1. Define the mapping of Badge Titles to Image Filenames
        # Ensure these titles match exactly what is in utils.py
        badges_config = [
            {
                'title': "🏆 Personalizador Pro",
                'image': 'phase1.png',
                'description': 'Mastered the basics of customization',
                'type': 'milestone'
            },
            {
                'title': "📁 Maestro de Archivos",
                'image': 'phase2.png',
                'description': 'Expert at file management',
                'type': 'milestone'
            },
            {
                'title': "⌨️ Velocidad de Hacker",
                'image': 'phase3.png',
                'description': 'Typing speed and shortcuts master',
                'type': 'milestone'
            },
            {
                'title': "🛡️ Escudo Digital",
                'image': 'phase4.png',
                'description': 'Navegación segura y defensa contra virus',
                'type': 'milestone'
            },
            {
                'title': "🛠️ Técnico Autosuficiente",
                'image': 'phase5.png',
                'description': 'Mantenimiento y optimización del PC',
                'type': 'milestone'
            },
        ]

        # 2. Define source directory for images
        # Create a folder named 'badge_assets' in your project root (same level as manage.py)
        source_dir = os.path.join(settings.BASE_DIR, 'badge_assets')
        
        if not os.path.exists(source_dir):
            self.stdout.write(self.style.ERROR(f'Directory not found: {source_dir}'))
            self.stdout.write(self.style.WARNING('Please create a "badge_assets" folder and put your .png files there.'))
            return

        self.stdout.write('Checking badges...')

        for config in badges_config:
            # Check if image file exists
            img_path = os.path.join(source_dir, config['image'])
            
            # Get or Create the Badge
            badge, created = Badge.objects.get_or_create(
                title=config['title'],
                defaults={
                    'description': config['description'],
                    'badge_type': config['type']
                }
            )

            # Update the icon if it's missing or if we want to ensure it's set
            if os.path.exists(img_path):
                # Only update if icon is missing to avoid re-uploading every time
                if not badge.icon:
                    self.stdout.write(f'Uploading icon for: {config["title"]}...')
                    with open(img_path, 'rb') as f:
                        # save=True saves the model instance
                        badge.icon.save(config['image'], File(f), save=True)
                else:
                    self.stdout.write(f'Icon already exists for: {config["title"]}')
            else:
                self.stdout.write(self.style.WARNING(f'Image file missing for {config["title"]}: {img_path}'))

        self.stdout.write(self.style.SUCCESS('Badge setup complete!'))
