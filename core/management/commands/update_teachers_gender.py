from core.models import Teacher
from django.db import transaction

@transaction.atomic
def update_teachers_gender():
    # List of emails from the existing teachers
    teacher_emails = [
        "angela.agbayani@inchs.com", "bernadette.aguas@inchs.com", "camille.alba@inchs.com",
        "diana.alcantara@inchs.com", "erica.andales@inchs.com", "faith.ang@inchs.com",
        "grace.apilan@inchs.com", "hanna.aranas@inchs.com", "isabelle.baclayon@inchs.com",
        "jade.baguio@inchs.com", "katrina.bailon@inchs.com", "louise.balondo@inchs.com",
        "maria.banua@inchs.com", "natalie.bascones@inchs.com", "olivia.batucan@inchs.com",
        "patricia.belderol@inchs.com", "queenie.bingo@inchs.com", "rhea.binuya@inchs.com",
        "sophia.bitang@inchs.com", "trisha.bughao@inchs.com", "ursula.cabacungan@inchs.com",
        "vanessa.cabaron@inchs.com", "wendy.cabrias@inchs.com", "xylena.caderao@inchs.com",
        "yasmine.cadungog@inchs.com", "zara.calungsod@inchs.com", "abigail.calvo@inchs.com",
        "bella.canete@inchs.com", "catherine.caylan@inchs.com", "danica.cid@inchs.com",
        "erica.dacula@inchs.com", "fiona.dagumboy@inchs.com", "grace.dalama@inchs.com",
        "hannah.datiles@inchs.com", "ivy.dazo@inchs.com", "julia.deiparine@inchs.com",
        "katrina.dumaog@inchs.com", "louise.echipare@inchs.com", "maria.fajardo@inchs.com",
        "nicole.ferrariz@inchs.com", "olivia.galarosa@inchs.com", "patricia.gamolo@inchs.com",
        "queen.gandia@inchs.com", "ruby.garces@inchs.com", "sarah.genson@inchs.com",
        "theresa.golingay@inchs.com", "ursula.juntilla@inchs.com", "valerie.labrado@inchs.com",
        "wendy.lapena@inchs.com", "yasmine.lumabas@inchs.com"
    ]

    try:
        # Get all teachers whose user's email is in the list
        updated_count = Teacher.objects.filter(
            user__email__in=teacher_emails
        ).update(Gender='Female')
        
        print(f"Successfully updated {updated_count} teachers' gender to Female")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

# Run the update
update_teachers_gender()