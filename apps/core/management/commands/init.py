from django.core.management import BaseCommand
from django.utils.text import slugify

from apps.company.models import CompanyDetail
from apps.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        # title = models.CharField(max_length=10, choices=TITLE_CHOICES)
        # full_name = models.CharField(max_length=255)
        # gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
        user, created = User.objects.get_or_create(
            username='testuser',
            email='testuser@gmail.com',
            title='Mr',
            gender='Male',
            full_name='test User'
        )
        user.set_password('password')
        user.save()

        name = 'Lipipoint PVT ltd'
        company, created = CompanyDetail.objects.get_or_create(
            user=user,
            name=name,
            logo='imgages/default/lipipoint.png',
            slug=slugify(name),
            email='lipipoint@gmail.com',
            phone1='1212121212')
        self.stdout.write(self.style.SUCCESS('Successfully created or get {} {}'.format(user, company)))
