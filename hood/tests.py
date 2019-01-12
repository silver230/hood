from django.test import TestCase

# Create your tests here.
class NeighbourhoodTest(TestCase):
    # def setUp(self):
    #     self.user=User(username='asumanisilver',first_name='silver',last_name='asumani',email='asumanisilver@gmail.com')
    #     self.user.save()
    #     self.new_Neighbourhood=Neighbourhood( Occupants_count="6",name='Moringa',location='Kenya')
    #     self.new_Neighbourhood = Neighbourhood( Occupants_count="6",name='Moringa',location='Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Neighbourhood,Neighbourhood))

    def test_data(self):
        self.assertTrue(self.new_Neighbourhood.location,'Kenya')

    def test_save(self):
        self.new_Neighbourhood.save()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete(self):
        hood = Neighbourhood.objects.filter(id=1)
        hood.delete()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

    def test_update_post(self):
        self.new_Neighbourhood.save()
        self.update_Neighbourhood = Neighbourhood.objects.filter(name='Moringa').update(name='kawangware')
        self.updated_Neighbourhood = Neighbourhood.objects.get(name='kawangware')
        self.assertTrue(self.updated_Neighbourhood.name,'kawangware')
