from core.models import User, Teacher
from django.db import transaction

teachers_data = [
 {"first_name": "Angela", "last_name": "Agbayani", "middle_initial": "Reyes", "email": "angela.agbayani@inchs.com"},
    {"first_name": "Bernadette", "last_name": "Aguas", "middle_initial": "Lim", "email": "bernadette.aguas@inchs.com"},
    {"first_name": "Camille", "last_name": "Alba", "middle_initial": "Garcia", "email": "camille.alba@inchs.com"},
    {"first_name": "Diana", "last_name": "Alcantara", "middle_initial": "Rivera", "email": "diana.alcantara@inchs.com"},
    {"first_name": "Erica", "last_name": "Andales", "middle_initial": "Salazar", "email": "erica.andales@inchs.com"},
    {"first_name": "Faith", "last_name": "Ang", "middle_initial": "Santos", "email": "faith.ang@inchs.com"},
    {"first_name": "Grace", "last_name": "Apilan", "middle_initial": "Uy", "email": "grace.apilan@inchs.com"},
    {"first_name": "Hanna", "last_name": "Aranas", "middle_initial": "Sy", "email": "hanna.aranas@inchs.com"},
    {"first_name": "Isabelle", "last_name": "Baclayon", "middle_initial": "Lim", "email": "isabelle.baclayon@inchs.com"},
    {"first_name": "Jade", "last_name": "Baguio", "middle_initial": "Torres", "email": "jade.baguio@inchs.com"},
    {"first_name": "Katrina", "last_name": "Bailon", "middle_initial": "Garcia", "email": "katrina.bailon@inchs.com"},
    {"first_name": "Louise", "last_name": "Balondo", "middle_initial": "Rivera", "email": "louise.balondo@inchs.com"},
    {"first_name": "Maria", "last_name": "Banua", "middle_initial": "Cruz", "email": "maria.banua@inchs.com"},
    {"first_name": "Natalie", "last_name": "Bascones", "middle_initial": "Salazar", "email": "natalie.bascones@inchs.com"},
    {"first_name": "Olivia", "last_name": "Batucan", "middle_initial": "Uy", "email": "olivia.batucan@inchs.com"},
    {"first_name": "Patricia", "last_name": "Belderol", "middle_initial": "Sy", "email": "patricia.belderol@inchs.com"},
    {"first_name": "Queenie", "last_name": "Bingo", "middle_initial": "Santos", "email": "queenie.bingo@inchs.com"},
    {"first_name": "Rhea", "last_name": "Binuya", "middle_initial": "Lim", "email": "rhea.binuya@inchs.com"},
    {"first_name": "Sophia", "last_name": "Bitang", "middle_initial": "Garcia", "email": "sophia.bitang@inchs.com"},
    {"first_name": "Trisha", "last_name": "Bughao", "middle_initial": "Uy", "email": "trisha.bughao@inchs.com"},
    {"first_name": "Ursula", "last_name": "Cabacungan", "middle_initial": "Reyes", "email": "ursula.cabacungan@inchs.com"},
    {"first_name": "Vanessa", "last_name": "Cabaron", "middle_initial": "Lim", "email": "vanessa.cabaron@inchs.com"},
    {"first_name": "Wendy", "last_name": "Cabrias", "middle_initial": "Salazar", "email": "wendy.cabrias@inchs.com"},
    {"first_name": "Xylena", "last_name": "Caderao", "middle_initial": "Torres", "email": "xylena.caderao@inchs.com"},
    {"first_name": "Yasmine", "last_name": "Cadungog", "middle_initial": "Uy", "email": "yasmine.cadungog@inchs.com"},
    {"first_name": "Zara", "last_name": "Calungsod", "middle_initial": "Garcia", "email": "zara.calungsod@inchs.com"},
    {"first_name": "Abigail", "last_name": "Calvo", "middle_initial": "Reyes", "email": "abigail.calvo@inchs.com"},
    {"first_name": "Bella", "last_name": "Cañete", "middle_initial": "Lim", "email": "bella.canete@inchs.com"},
    {"first_name": "Catherine", "last_name": "Caylan", "middle_initial": "Salazar", "email": "catherine.caylan@inchs.com"},
    {"first_name": "Danica", "last_name": "Cid", "middle_initial": "Uy", "email": "danica.cid@inchs.com"},
    {"first_name": "Erica", "last_name": "Dacula", "middle_initial": "Torres", "email": "erica.dacula@inchs.com"},
    {"first_name": "Fiona", "last_name": "Dagumboy", "middle_initial": "Garcia", "email": "fiona.dagumboy@inchs.com"},
    {"first_name": "Grace", "last_name": "Dalama", "middle_initial": "Reyes", "email": "grace.dalama@inchs.com"},
    {"first_name": "Hannah", "last_name": "Datiles", "middle_initial": "Sy", "email": "hannah.datiles@inchs.com"},
    {"first_name": "Ivy", "last_name": "Dazo", "middle_initial": "Lim", "email": "ivy.dazo@inchs.com"},
    {"first_name": "Julia", "last_name": "Deiparine", "middle_initial": "Salazar", "email": "julia.deiparine@inchs.com"},
    {"first_name": "Katrina", "last_name": "Dumaog", "middle_initial": "Santos", "email": "katrina.dumaog@inchs.com"},
    {"first_name": "Louise", "last_name": "Echipare", "middle_initial": "Uy", "email": "louise.echipare@inchs.com"},
    {"first_name": "Maria", "last_name": "Fajardo", "middle_initial": "Lim", "email": "maria.fajardo@inchs.com"},
    {"first_name": "Nicole", "last_name": "Ferrariz", "middle_initial": "Garcia", "email": "nicole.ferrariz@inchs.com"},
    {"first_name": "Olivia", "last_name": "Galarosa", "middle_initial": "Salazar", "email": "olivia.galarosa@inchs.com"},
    {"first_name": "Patricia", "last_name": "Gamolo", "middle_initial": "Uy", "email": "patricia.gamolo@inchs.com"},
    {"first_name": "Queen", "last_name": "Gandia", "middle_initial": "Reyes", "email": "queen.gandia@inchs.com"},
    {"first_name": "Ruby", "last_name": "Garces", "middle_initial": "Lim", "email": "ruby.garces@inchs.com"},
    {"first_name": "Sarah", "last_name": "Genson", "middle_initial": "Santos", "email": "sarah.genson@inchs.com"},
    {"first_name": "Theresa", "last_name": "Golingay", "middle_initial": "Uy", "email": "theresa.golingay@inchs.com"},
    {"first_name": "Ursula", "last_name": "Juntilla", "middle_initial": "Salazar", "email": "ursula.juntilla@inchs.com"},
    {"first_name": "Valerie", "last_name": "Labrado", "middle_initial": "Sy", "email": "valerie.labrado@inchs.com"},
    {"first_name": "Wendy", "last_name": "Lapeña", "middle_initial": "Reyes", "email": "wendy.lapena@inchs.com"},
    {"first_name": "Yasmine", "last_name": "Lumabas", "middle_initial": "Torres", "email": "yasmine.lumabas@inchs.com"}
]

# Base phone number
base_phone_number = 900001251

# Password for all users
default_password = "12teacher12"

@transaction.atomic
def create_teachers():
    for index, teacher in enumerate(teachers_data):
        email = teacher["email"]
        first_name = teacher["first_name"]
        last_name = teacher["last_name"]
        middle_initial = teacher["middle_initial"]
        phone_number = f"09{base_phone_number + index}"  # Ensure phone starts with 09

        # Create User
        user = User.objects.create_user(
            email=email,
            password=default_password,
            is_teacher=True
        )


        Teacher.objects.create(
            user=user,
            Firstname=first_name,
            Lastname=last_name,
            Middle_Initial=middle_initial,
            Gender="Male",  # Dummy gender assignment
            Phone_Number=phone_number
        )
    print("Teacher and users created successfully!")

# Run the script
create_teachers()
