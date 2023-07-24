
from django.db import models
from accounts.models import ProfileModel

class concertModel(models.Model):
    class Meta:
        verbose_name = "Concert"
    
    # The name of the concert
    Name = models.CharField(max_length=100, null=True)
    
    # The name of the singer performing in the concert
    SingerName = models.CharField(max_length=100, null=True)
    
    # The duration of the concert in minutes
    length = models.IntegerField(null=True)
    
    # The poster image of the concert
    Poster = models.ImageField(upload_to="concertimages/", null=True)

    def __str__(self):
        return self.SingerName

class locationModel(models.Model):
    class Meta:
        verbose_name = "Location"
    
    # The concert associated with this location
    concertModel = models.ForeignKey('concertModel', on_delete=models.CASCADE, null=True)
    
    # The name of the location
    Name = models.CharField(max_length=100, null=True)
    
    # The address of the location
    Address = models.CharField(max_length=500, default='Antalya')
    
    # The phone number of the location
    Phone = models.CharField(max_length=11, null=True)
    
    # The capacity of the location
    Capacity = models.IntegerField(null=True)

    def __str__(self):
        return self.Name

    
class timeModel(models.Model):
    class Meta:
        verbose_name = "Time"
    
    # The concert associated with this time
    concertModel = models.ForeignKey('concertModel', on_delete=models.CASCADE, null=True)
    
    # The location associated with this time
    locationModel = models.ForeignKey('locationModel', on_delete=models.CASCADE, null=True)
    
    # The start date and time of the concert
    StartDateTime = models.DateTimeField(null=True)
    
    # The number of available seats for the concert
    Seats = models.IntegerField(default=1)

    # Constants representing the status of ticket sales
    Start = 1
    End = 2
    Cancel = 3
    Saling = 4
    
    # Choices for the status of ticket sales
    status_choices = ((Start, "Ticket sales have started"),
                      (End, "Ticket sales are over"),
                      (Cancel, "Ticket sales have been cancelled"),
                      (Saling, "Ticket sales have been saling"))

    # The current status of ticket sales
    Status = models.IntegerField(choices=status_choices, default=1)

    def __str__(self):
        return self.concertModel.SingerName + " in " + self.locationModel.Name + " on " + self.StartDateTime.strftime("%Y-%m-%d %H:%M:%S")


class ticketModel(models.Model):
    class Meta:
        verbose_name = "Ticket"
    
    # The profile associated with this ticket
    profileModel = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    
    # The time associated with this ticket
    timeModel = models.ForeignKey('timeModel', on_delete=models.CASCADE)
    
    # The image of the ticket
    TicketImage = models.ImageField(upload_to="ticketimages/", null=True)
    
    # The name of the ticket
    Name = models.CharField(max_length=100)
    
    # The price of the ticket
    Price = models.IntegerField()

    def __str__(self):
        return "Ticket info: Profile : {} Concert info : {}".format(timeModel.__str__())
