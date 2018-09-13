from marshmallow import Schema,fields,validates,ValidationError
# import datetime

class RideSchema(Schema):
    start_point = fields.String(required=True)
    destination = fields.String(required=True)
    seats_available=fields.String(required=True)
    date=fields.String(required=True)
    time=fields.String(required=True)

    @validates("start_point")
    def validate_start_point(self,start_point):
        if start_point.strip == "":
            raise ValidationError("start point cannot be blank")
        elif len(start_point)<3:
            raise ValidationError("start point should be at least 3 characters long")

    @validates("destination")
    def validate_destination(self,destination):
        if destination.strip == "":
            raise ValidationError(" destination cannot be blank")
        elif len(destination)<3:
            raise ValidationError("destination should be at least 3 characters long")

    @validates("seats_available")
    def seats_available(self, seats_available):
        if int(seats_available)<1:
            raise ValidationError(" seats_available cannot be less than one")

    # @validates("date")
    # def date(self, date):
    #     if not datetime.datetime.strptime(date, '%d/%m/%Y'):
    #         raise ValidationError(" please enter a valid date eg 11/12/2019")
    #
    # @validates("time")
    # def date(self, time):
    #     if not datetime.datetime.strptime(time, 'H:M'):
    #         raise ValidationError(" please enter valid time eg 10:00")
    #








