from django.urls import reverse
from rest_framework import test


class ProductAPIv1Test(test.APITestCase):
    def test_api_list_returns_status_code_200(self):
        api_url = reverse('products:product-api-list')
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, 200)

    def test_api_detail_returns_status_code_404(self):
        api_url = reverse('products:product-api-detail', args=[1])
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, 404)
