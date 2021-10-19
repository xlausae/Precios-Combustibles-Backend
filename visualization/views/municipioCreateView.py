from rest_framework import status, views
from rest_framework.response import Response
from visualization.serializers.municipiosSerializer import MunicipiosSerializer


class MunicipioCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = MunicipiosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)