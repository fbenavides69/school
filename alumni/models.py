from django.db import models
import datetime
from .constants import *

# Create your models here.


class ScholarCycle(models.Model):
    """
    ScholarCycle
    Yearly School Cycle (e.g. 2012-2013)
    """
    cycle = models.CharField(blank=False, max_length=9, verbose_name='Ciclo Escolar')

    def __repr__(self):
        return '{:s}'.format(self.cycle)

    def __str__(self):
        return '{:s}'.format(self.cycle)

    class Meta:
        db_table = 'Ciclo Escolar'
        ordering = ['cycle']
        verbose_name = 'Ciclo Escolar'
        verbose_name_plural = 'Ciclos Escolares'

    class Admin:
        pass


class Alumni(models.Model):
    """ Alumni
        School Children
    """
    cycle = models.ForeignKey(
        ScholarCycle, unique=False, null=False, blank=True, verbose_name='Ciclo Escolar', on_delete=models.CASCADE)
    register_date = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, verbose_name='Fecha de Inscripción')
    modified_date = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name='Fecha de Última Modificación')
    folio = models.CharField(
        null=False, blank=False, max_length=8, verbose_name='Número de Folio')

    agreement = models.IntegerField(
        choices=ALUMNI_AGREEMENT_CHOICES, default=ALUMNI_AGREEMENT_PARTICULAR, verbose_name='Convenio')
    child_name = models.CharField(
        blank=False, max_length=30, verbose_name='Nombre(s)')
    child_familynames = models.CharField(
        blank=False, max_length=30, verbose_name='Apellidos')
    child_dob = models.DateField(
        blank=False, verbose_name='Fecha de Nacimiento')
    child_curp_id = models.CharField(
        blank=False, max_length=30, verbose_name='CURP')
    child_gender = models.IntegerField(
        choices=ALUMNI_GENDER_CHOICES, default=ALUMNI_GENDER_FEMALE, verbose_name='Sexo')
    child_schedule = models.IntegerField(
        choices=ALUMNI_SCHEDULE_CHOICES, default=ALUMNI_SCHEDULE_NORMAL, verbose_name='Horario')
    child_group = models.IntegerField(
        choices=ALUMNI_GROUP_CHOICES, default=ALUMNI_GROUP_PRESCHOOL_1, verbose_name='Grupo')
    child_blood_type = models.IntegerField(
        choices=ALUMNI_BLOOD_TYPE_CHOICES, default=ALUMNI_BLOOD_TYPE_O_POSITIVE, verbose_name='Tipo de Sangre')
    child_photo = models.ImageField(
        blank=True, upload_to='photos', verbose_name='Foto')
    child_observations = models.TextField(
        blank=True, verbose_name='Observaciones')
    emergency_telephone_number = models.CharField(
        blank=True, max_length=15, verbose_name='Número de Emergencia')
    emergency_contact = models.CharField(
        blank=True, max_length=30, verbose_name='Nombre del Contacto de Emergencia')
    doctor = models.CharField(
        blank=True, max_length=30, verbose_name='Médico')
    hospital = models.CharField(
        blank=True, max_length=30, verbose_name='Hospital')

    house_telephone = models.CharField(
        blank=True, max_length=15, verbose_name='Teléfono de casa')
    street_name = models.CharField(
        blank=True, max_length=30, verbose_name='Calle')
    street_exterior_number = models.CharField(
        blank=True, max_length=10, verbose_name='Número Exterior')
    street_interior_number = models.CharField(
        blank=True, max_length=5, verbose_name='Número Interior')
    area_colonia = models.CharField(
        blank=True, max_length=60, verbose_name='Colonia')
    zip_code = models.CharField(
        blank=True, max_length=10, verbose_name='Código Postal')
    description = models.TextField(
        blank=True, verbose_name='Notas')
    mapa = models.URLField(
        blank=True, verbose_name='Mapa')
    father_name = models.CharField(
        blank=True, max_length=30, verbose_name='Nombre(s) Papá')
    father_familynames = models.CharField(
        blank=True, max_length=30, verbose_name='Apellidos')
    father_cell_phone = models.CharField(
        blank=True, max_length=15, verbose_name='Télefono Celular')
    father_telephone_work = models.CharField(
        blank=True, max_length=15, verbose_name='Télefono Trabajo')
    father_telephone_extension = models.CharField(
        blank=True, max_length=6, verbose_name='Extensión')
    father_email = models.EmailField(
        blank=True, max_length=60, verbose_name='Dirección Electrónica')
    father_occupation = models.CharField(
        blank=True, max_length=30, verbose_name='Ocupación')
    father_photo = models.ImageField(
        blank=True, upload_to='photos', verbose_name='Archivo Foto')
    father_ife_id = models.CharField(
        blank=True, max_length=30, verbose_name='IFE')
    father_ife_file = models.FileField(
        blank=True, upload_to='docs', verbose_name='Archivo IFE')
    father_curp_id = models.CharField(
        blank=True, max_length=30, verbose_name='CURP')
    mother_name = models.CharField(
        blank=True, max_length=30, verbose_name='Nombre(s) Mamá')
    mother_familynames = models.CharField(
        blank=True, max_length=30, verbose_name='Apellidos')
    mother_cell_phone = models.CharField(
        blank=True, max_length=15, verbose_name='Télefono Celular')
    mother_telephone_work = models.CharField(
        blank=True, max_length=15, verbose_name='Télefono Trabajo')
    mother_telephone_extension = models.CharField(
        blank=True, max_length=6, verbose_name='Extensión')
    mother_email = models.EmailField(
        blank=True, max_length=60, verbose_name='Dirección Electrónica')
    mother_occupation = models.CharField(
        blank=True, max_length=30, verbose_name='Ocupación')
    mother_photo = models.ImageField(
        blank=True, upload_to='photos', verbose_name='Archivo Foto')
    mother_ife_id = models.CharField(
        blank=True, max_length=30, verbose_name='IFE')
    mother_ife_file = models.FileField(
        blank=True, upload_to='docs', verbose_name='Archivo IFE')
    mother_curp_id = models.CharField(
        blank=True, max_length=30, verbose_name='CURP')

    authorized1_name = models.CharField(
        blank=True, max_length=30, verbose_name='Nombre(s) Persona Autorizada')
    authorized1_familynames = models.CharField(
        blank=True, max_length=30, verbose_name='Apellidos')
    authorized1_cell_phone = models.CharField(
        blank=True, max_length=15, verbose_name='Teléfono Celular')
    authorized1_telephone = models.CharField(
        blank=True, max_length=15, verbose_name='Teléfono')
    authorized1_parentezco = models.IntegerField(
        null=True, blank=True, choices=PARENTEZCO_CHOICES, verbose_name='Parentezco')
    authorized2_name = models.CharField(
        blank=True, max_length=30, verbose_name='Nombre(s) Persona Autorizada')
    authorized2_familynames = models.CharField(
        blank=True, max_length=30, verbose_name='Apellidos')
    authorized2_cell_phone = models.CharField(
        blank=True, max_length=15, verbose_name='Teléfono Celular')
    authorized2_telephone = models.CharField(
        blank=True, max_length=15, verbose_name='Teléfono')
    authorized2_parentezco = models.IntegerField(
        null=True, blank=True, choices=PARENTEZCO_CHOICES, verbose_name='Parentezco')

    colegiatura = models.IntegerField(
        null=True, blank=True, verbose_name='Colegiatura')
    august_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Agosto')
    august_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    august_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    september_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Septiembre')
    september_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    september_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    october_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Octubre')
    october_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    october_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    november_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Noviembre')
    november_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    november_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    december_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Diciembre')
    december_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    december_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    january_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Enero')
    january_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    january_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    february_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Febrero')
    february_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    february_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    march_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Marzo')
    march_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    march_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    april_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Abril')
    april_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    april_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    may_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Mayo')
    may_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    may_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    june_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Junio')
    june_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    june_annotations = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    register_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Inscripción Pagada')
    register_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    register_notes = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    insurance_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Seguro Pagado')
    insurance_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    insurance_notes = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    uniform_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Uniforme Pagado')
    uniform_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    uniform_notes = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    supplies_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Material Pagado')
    supplies_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    supplies_notes = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    events_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Evento Pagado')
    events_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    events_notes = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')
    otros_payed = models.IntegerField(
        null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name='Otros Pagado')
    otros_payed_date = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Pago')
    otros_notes = models.TextField(
        blank=True, max_length=400, verbose_name='Notas')

    birth_certificate = models.FileField(
        blank=True, upload_to='docs', verbose_name='Acta de Nacimiento')
    immunization_card = models.FileField(
        blank=True, upload_to='docs', verbose_name='Cartilla de Vacunación')
    curp_card = models.FileField(
        blank=True, upload_to='docs', verbose_name='CURP')

    def group_string(self):
        return ALUMNI_GROUP_CHOICES[self.child_group][1]

    def schedule_string(self):
        return ALUMNI_SCHEDULE_CHOICES[self.child_schedule][1]

    def agreement_string(self):
        return ALUMNI_AGREEMENT_CHOICES[self.agreement][1]

    def set_payed_date(self):
        if self.august_payed == ALUMNI_PAYED:
            if self.august_payed_date is None:
                self.august_payed_date = datetime.datetime.now()
        if self.september_payed == ALUMNI_PAYED:
            if self.september_payed_date is None:
                self.september_payed_date = datetime.datetime.now()
        if self.october_payed == ALUMNI_PAYED:
            if self.october_payed_date is None:
                self.october_payed_date = datetime.datetime.now()
        if self.november_payed == ALUMNI_PAYED:
            if self.november_payed_date is None:
                self.november_payed_date = datetime.datetime.now()
        if self.december_payed == ALUMNI_PAYED:
            if self.december_payed_date is None:
                self.december_payed_date = datetime.datetime.now()
        if self.january_payed == ALUMNI_PAYED:
            if self.january_payed_date is None:
                self.january_payed_date = datetime.datetime.now()
        if self.february_payed == ALUMNI_PAYED:
            if self.february_payed_date is None:
                self.february_payed_date = datetime.datetime.now()
        if self.march_payed == ALUMNI_PAYED:
            if self.march_payed_date is None:
                self.march_payed_date = datetime.datetime.now()
        if self.april_payed == ALUMNI_PAYED:
            if self.april_payed_date is None:
                self.april_payed_date = datetime.datetime.now()
        if self.may_payed == ALUMNI_PAYED:
            if self.may_payed_date is None:
                self.may_payed_date = datetime.datetime.now()
        if self.june_payed == ALUMNI_PAYED:
            if self.june_payed_date is None:
                self.june_payed_date = datetime.datetime.now()
        if self.register_payed == ALUMNI_PAYED:
            if self.register_payed_date is None:
                self.register_payed_date = datetime.datetime.now()
        if self.insurance_payed == ALUMNI_PAYED:
            if self.insurance_payed_date is None:
                self.insurance_payed_date = datetime.datetime.now()
        if self.uniform_payed == ALUMNI_PAYED:
            if self.uniform_payed_date is None:
                self.uniform_payed_date = datetime.datetime.now()
        if self.supplies_payed == ALUMNI_PAYED:
            if self.supplies_payed_date is None:
                self.supplies_payed_date = datetime.datetime.now()
        if self.events_payed == ALUMNI_PAYED:
            if self.events_payed_date is None:
                self.events_payed_date = datetime.datetime.now()

    def get_child_photo_file(self):
        return os.path.basename(self.child_photo.name)

    def get_father_photo_file(self):
        return os.path.basename(self.father_photo.name)

    def get_mother_photo_file(self):
        return os.path.basename(self.mother_photo.name)

    def get_birth_certificate_file(self):
        return os.path.basename(self.birth_certificate.name)

    def get_curp_card_file(self):
        return os.path.basename(self.curp_card.name)

    def get_immunization_card_file(self):
        return os.path.basename(self.immunization_card.name)

    def get_father_ife_file(self):
        return os.path.basename(self.father_ife_file.name)

    def get_mother_ife_file(self):
        return os.path.basename(self.mother_ife_file.name)

    def get_parentezco1_string(self):
        if self.authorized1_parentezco:
            return PARENTEZCO_CHOICES[self.authorized1_parentezco][1]
        return ''

    def get_parentezco2_string(self):
        if self.authorized2_parentezco:
            return PARENTEZCO_CHOICES[self.authorized2_parentezco][1]
        return ''

    def get_august_payed_string(self):
        return ALUMNI_CHOICES[self.august_payed][1]

    def get_september_payed_string(self):
        return ALUMNI_CHOICES[self.september_payed][1]

    def get_october_payed_string(self):
        return ALUMNI_CHOICES[self.october_payed][1]

    def get_november_payed_string(self):
        return ALUMNI_CHOICES[self.november_payed][1]

    def get_december_payed_string(self):
        return ALUMNI_CHOICES[self.december_payed][1]

    def get_january_payed_string(self):
        return ALUMNI_CHOICES[self.january_payed][1]

    def get_february_payed_string(self):
        return ALUMNI_CHOICES[self.february_payed][1]

    def get_march_payed_string(self):
        return ALUMNI_CHOICES[self.march_payed][1]

    def get_april_payed_string(self):
        return ALUMNI_CHOICES[self.april_payed][1]

    def get_may_payed_string(self):
        return ALUMNI_CHOICES[self.may_payed][1]

    def get_june_payed_string(self):
        return ALUMNI_CHOICES[self.june_payed][1]

    def get_register_payed_string(self):
        return ALUMNI_CHOICES[self.register_payed][1]

    def get_insurance_payed_string(self):
        return ALUMNI_CHOICES[self.insurance_payed][1]

    def get_uniform_payed_string(self):
        return ALUMNI_CHOICES[self.uniform_payed][1]

    def get_supplies_payed_string(self):
        return ALUMNI_CHOICES[self.supplies_payed][1]

    def get_events_payed_string(self):
        return ALUMNI_CHOICES[self.events_payed][1]

    def get_otros_payed_string(self):
        return ALUMNI_CHOICES[self.otros_payed][1]

    def get_absolute_url(self):
        return reverse('alumni-details', kwargs={'id': self.id})

    def set_cycle(self):
        try:
            self.cycle = ScholarCycle.objects.latest('id')
        except:
            self.cycle = None

    def set_folio(self):
        try:
            lastFolio = Alumni.objects.latest('id').folio.split(':')
        except:
            lastFolio = None
        year = datetime.datetime.now().year
        if lastFolio is None:
            self.folio = str(year) + ':000'
        elif int(lastFolio[0]) == year:
            number = int(lastFolio[1]) + 1
            self.folio = str(year) + ':' + str(number).zfill(3)
        else:
            self.folio = str(year) + ':000'

    def set_uppercase(self):
        self.child_name = self.child_name.upper()
        self.child_familynames = self.child_familynames.upper()
        self.father_name = self.father_name.upper()
        self.father_familynames = self.father_familynames.upper()
        self.mother_name = self.mother_name.upper()
        self.mother_familynames = self.mother_familynames.upper()
        self.authorized1_name = self.authorized1_name.upper()
        self.authorized1_familynames = self.authorized1_familynames.upper()
        self.authorized2_name = self.authorized2_name.upper()
        self.authorized2_familynames = self.authorized2_familynames.upper()

    def age(self):
        if self.child_dob > datetime.date.today().replace(year=self.child_dob.year):
            return datetime.date.today().year - self.child_dob.year - 1
        else:
            return datetime.date.today().year - self.child_dob.year

    def save(self, *args, **kwargs):
        if not self.id:
            self.set_folio()
        self.set_uppercase()
        self.set_cycle()
        self.set_payed_date()
        super(Alumni, self).save(*args, **kwargs)

    def __repr__(self):
        return '{:8s} {:20s} {:30s} {:20s}'.format(
            self.folio,
            self.child_name,
            self.child_familynames,
            self.group_string())

    def __str__(self):
        return '{:8s} {:20s} {:30s} {:20s}'.format(
            self.folio,
            self.child_name,
            self.child_familynames,
            self.group_string())

    class Meta:
        db_table = 'Alumno'
        ordering = ['child_name', 'child_familynames']
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    class Admin:
        pass
