from django.db import models

# Create your models here.
class Images(models.Model):
    '''
    model to handle images
    '''
    image_link = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    description = models.TextField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, default=1)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title

    def save_image(self):
        '''
        method to save an image
        '''
        self.save()

    def delete_image(self):
        '''
        method to delete an image
        '''
        self.delete()

    def update_image(self, new_url):
        '''
        method to update an image's link
        '''
        try:
            self.image_link = new_url
            self.save()
            return self
        except self.DoesNotExist:
            print('Image you specified does not exist')

    @classmethod
    def get_all(cls):
        '''
        method to retrieve all images
        '''
        pics = Images.objects.all()
        return pics

    @classmethod
    def get_image_by_id(cls, id):
        '''
        method to retrieve images by unique id
        '''
        retrieved = Images.objects.get(id = id)
        return retrieved

    @classmethod
    def search_image(cls, cat):
        '''
        method to search images by category
        '''
        retrieved = cls.objects.filter(category__name__contains=cat) #images assoc w/ this cat
        return retrieved #list of instances

    @classmethod
    def filter_by_location(cls ,location):
        '''
        method to retrive images by their locations
        '''
        retrieved = Images.objects.filter(location__city__contains=location)
        return retrieved


class Categories(models.Model):
    '''
    model to handle categories
    '''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        '''
        method to save a category
        '''
        self.save()

    def delete_category(self):
        '''
        method to delete a category
        '''
        self.delete()

    @classmethod
    def update_category(cls, search_term , new_cat):
        '''
        method to update a category
        '''
        try:
            to_update = Categories.objects.get(name = search_term)
            to_update.name = new_cat
            to_update.save()
            return to_update
        except Categories.DoesNotExist:
            print('Category you specified does not exist')



class Locations(models.Model):
    '''
    model to handle locations
    '''
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.city

    def save_location(self):
        '''
        method to save a location
        '''
        self.save()

    def delete_location(self):
        '''
        method to delete a location
        '''
        self.delete()

    @classmethod
    def update_location(cls, search_term , new_locale):
        '''
        method to update a location's city name
        '''
        try:
            to_update = Locations.objects.get(country = search_term)
            to_update.city = new_locale
            to_update.save()
            return to_update
        except Locations.DoesNotExist:
            print('Location you specified does not exist')

    @classmethod
    def get_all(cls):
        '''
        method to retrive all stored locations
        '''
        cities = Locations.objects.all()
        return cities