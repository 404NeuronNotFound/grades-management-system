from core.models import User, Student
from django.db import transaction

# List of student data
students_data = [
  {"first_name": "Angela Rose", "last_name": "Abacahin", "middle_initial": "Lopez", "email": "angela.abacahin@student.inchs.com"},
    {"first_name": "Bernadette Anne", "last_name": "Abasolo", "middle_initial": "Uy", "email": "bernadette.abasolo@student.inchs.com"},
    {"first_name": "Camille Joy", "last_name": "Agbada", "middle_initial": "Rivera", "email": "camille.agbada@student.inchs.com"},
    {"first_name": "Diana May", "last_name": "Albia", "middle_initial": "Garcia", "email": "diana.albia@student.inchs.com"},
    {"first_name": "Erica Faye", "last_name": "Alingalan", "middle_initial": "Santos", "email": "erica.alingalan@student.inchs.com"},
    {"first_name": "Faith Marie", "last_name": "Amoro", "middle_initial": "Tan", "email": "faith.amoro@student.inchs.com"},
    {"first_name": "Grace Ann", "last_name": "Ando", "middle_initial": "Sy", "email": "grace.ando@student.inchs.com"},
    {"first_name": "Hanna Leigh", "last_name": "Anora", "middle_initial": "Villanueva", "email": "hanna.anora@student.inchs.com"},
    {"first_name": "Isabelle Joy", "last_name": "Apatan", "middle_initial": "Cruz", "email": "isabelle.apatan@student.inchs.com"},
    {"first_name": "Jade Marie", "last_name": "Apelo", "middle_initial": "Uy", "email": "jade.apelo@student.inchs.com"},
    {"first_name": "Katrina Mae", "last_name": "Balacuit", "middle_initial": "Rivera", "email": "katrina.balacuit@student.inchs.com"},
    {"first_name": "Louise Anne", "last_name": "Balingbing", "middle_initial": "Garcia", "email": "louise.balingbing@student.inchs.com"},
    {"first_name": "Maria Faye", "last_name": "Baliong", "middle_initial": "Tan", "email": "maria.baliong@student.inchs.com"},
    {"first_name": "Natalie Rose", "last_name": "Bantilan", "middle_initial": "Uy", "email": "natalie.bantilan@student.inchs.com"},
    {"first_name": "Olivia Anne", "last_name": "Batina", "middle_initial": "Santos", "email": "olivia.batina@student.inchs.com"},
    {"first_name": "Patricia Ann", "last_name": "Bayotas", "middle_initial": "Rivera", "email": "patricia.bayotas@student.inchs.com"},
    {"first_name": "Queenie Mae", "last_name": "Becera", "middle_initial": "Uy", "email": "queenie.becera@student.inchs.com"},
    {"first_name": "Rhea Ann", "last_name": "Cabalida", "middle_initial": "Tan", "email": "rhea.cabalida@student.inchs.com"},
    {"first_name": "Sophia Jane", "last_name": "Caballero", "middle_initial": "Cruz", "email": "sophia.caballero@student.inchs.com"},
    {"first_name": "Trisha Marie", "last_name": "Cabudti", "middle_initial": "Uy", "email": "trisha.cabudti@student.inchs.com"},
    {"first_name": "Ursula Mae", "last_name": "Caipang", "middle_initial": "Rivera", "email": "ursula.caipang@student.inchs.com"},
    {"first_name": "Vanessa Faye", "last_name": "Calipay", "middle_initial": "Garcia", "email": "vanessa.calipay@student.inchs.com"},
    {"first_name": "Wendy Joy", "last_name": "Cancio", "middle_initial": "Uy", "email": "wendy.cancio@student.inchs.com"},
    {"first_name": "Xylena Anne", "last_name": "Capistrano", "middle_initial": "Villanueva", "email": "xylena.capistrano@student.inchs.com"},
    {"first_name": "Yasmine Rose", "last_name": "Capuyan", "middle_initial": "Cruz", "email": "yasmine.capuyan@student.inchs.com"},
    {"first_name": "Zara Marie", "last_name": "Carcueva", "middle_initial": "Uy", "email": "zara.carcueva@student.inchs.com"},
    {"first_name": "Abigail May", "last_name": "Catipon", "middle_initial": "Rivera", "email": "abigail.catipon@student.inchs.com"},
    {"first_name": "Bella Faye", "last_name": "Catura", "middle_initial": "Tan", "email": "bella.catura@student.inchs.com"},
    {"first_name": "Catherine Jane", "last_name": "Caya", "middle_initial": "Uy", "email": "catherine.caya@student.inchs.com"},
    {"first_name": "Danica Ann", "last_name": "Cayog", "middle_initial": "Garcia", "email": "danica.cayog@student.inchs.com"},
    {"first_name": "Erica May", "last_name": "Cielo", "middle_initial": "Santos", "email": "erica.cielo@student.inchs.com"},
    {"first_name": "Fiona Leigh", "last_name": "Dalayo", "middle_initial": "Uy", "email": "fiona.dalayo@student.inchs.com"},
    {"first_name": "Grace Anne", "last_name": "Dalina", "middle_initial": "Rivera", "email": "grace.dalina@student.inchs.com"},
    {"first_name": "Hannah Mae", "last_name": "Dapar", "middle_initial": "Tan", "email": "hannah.dapar@student.inchs.com"},
    {"first_name": "Ivy Leigh", "last_name": "Diano", "middle_initial": "Uy", "email": "ivy.diano@student.inchs.com"},
    {"first_name": "Julia Faye", "last_name": "Dilao", "middle_initial": "Santos", "email": "julia.dilao@student.inchs.com"},
    {"first_name": "Katrina Jane", "last_name": "Dipat", "middle_initial": "Rivera", "email": "katrina.dipat@student.inchs.com"},
    {"first_name": "Louise Faye", "last_name": "Duncano", "middle_initial": "Uy", "email": "louise.duncano@student.inchs.com"},
    {"first_name": "Maria Anne", "last_name": "Emata", "middle_initial": "Tan", "email": "maria.emata@student.inchs.com"},
    {"first_name": "Nicole May", "last_name": "Garing", "middle_initial": "Santos", "email": "nicole.garing@student.inchs.com"},
    {"first_name": "Olivia Faye", "last_name": "Gaylardo", "middle_initial": "Uy", "email": "olivia.gaylardo@student.inchs.com"},
    {"first_name": "Patricia Jane", "last_name": "Gelindon", "middle_initial": "Rivera", "email": "patricia.gelindon@student.inchs.com"},
    {"first_name": "Ruby Faye", "last_name": "Ginete", "middle_initial": "Uy", "email": "ruby.ginete@student.inchs.com"},
    {"first_name": "Sarah Jane", "last_name": "Icatlo", "middle_initial": "Rivera", "email": "sarah.icatlo@student.inchs.com"},
    {"first_name": "Theresa Ann", "last_name": "Labadan", "middle_initial": "Uy", "email": "theresa.labadan@student.inchs.com"},
    {"first_name": "Ursula May", "last_name": "Labrague", "middle_initial": "Santos", "email": "ursula.labrague@student.inchs.com"},
    {"first_name": "Victoria Anne", "last_name": "Lano", "middle_initial": "Tan", "email": "victoria.lano@student.inchs.com"},
    {"first_name": "Wendy Faye", "last_name": "Mabong", "middle_initial": "Uy", "email": "wendy.mabong@student.inchs.com"},
    {"first_name": "Xyla Jane", "last_name": "Maganda", "middle_initial": "Santos", "email": "xyla.maganda@student.inchs.com"},
    {"first_name": "Yasmin May", "last_name": "Maglaque", "middle_initial": "Tan", "email": "yasmin.maglaque@student.inchs.com"}
]

# Base phone number
base_phone_number = 900001351

# Password for all users
default_password = "12student12"

@transaction.atomic
def create_students():
    for index, student in enumerate(students_data):
        email = student["email"]
        first_name = student["first_name"]
        last_name = student["last_name"]
        middle_initial = student["middle_initial"]
        phone_number = f"09{base_phone_number + index}"  # Ensure phone starts with 09

        # Create User
        user = User.objects.create_user(
            email=email,
            password=default_password,
            is_student=True
        )

        # Create Student
        Student.objects.create(
            user=user,
            Firstname=first_name,
            Lastname=last_name,
            Middle_Initial=middle_initial,
            Gender="Female",  # Dummy gender assignment
            Phone_Number=phone_number
        )
    print("Students and users created successfully!")

# Run the script
create_students()
