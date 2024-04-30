from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ComusDisModel, ComusCtrlParsModel, ComusOutParsModel
from .serializers import ComusModelSerializer, ComusCtrlParsSerializer, ComusOutParsSerializer


class ComusModelView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = ComusModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'COMUS Model Created Successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComusCtrlParsView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        user_name = request.query_params.get('user_name')
        project_name = request.query_params.get('project_name')
        try:
            comus_dis = ComusDisModel.objects.get(user_name=user_name, project_name=project_name)
            ctrl_pars = ComusCtrlParsModel.objects.filter(comus_dis_uuid=comus_dis.uuid)
            serializer = ComusCtrlParsSerializer(ctrl_pars, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'This COMUS model not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        user_name = request.data.get('user_name')
        project_name = request.data.get('project_name')
        comus_dis, _ = ComusDisModel.objects.get_or_create(user_name=user_name, project_name=project_name)
        request.data['comus_dis_uuid'] = comus_dis.uuid
        serializer = ComusCtrlParsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'COMUS control parameters saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user_name = request.data.get('user_name')
        project_name = request.data.get('project_name')

        try:
            comus_dis, _ = ComusDisModel.objects.get_or_create(user_name=user_name, project_name=project_name)
            request.data['comus_dis_uuid'] = comus_dis.uuid
        except:
            return Response({'error': 'This COMUS model not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            ctrl_pars = ComusCtrlParsModel.objects.get(comus_dis_uuid=comus_dis.uuid)
        except:
            return Response({'error': 'The control parameters of this COMUS model were not found!'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = ComusCtrlParsSerializer(ctrl_pars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'COMUS control parameters updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComusOutParsView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        user_name = request.query_params.get('user_name')
        project_name = request.query_params.get('project_name')
        try:
            comus_dis = ComusDisModel.objects.get(user_name=user_name, project_name=project_name)
            ctrl_pars = ComusOutParsModel.objects.filter(comus_dis_uuid=comus_dis.uuid)
            serializer = ComusOutParsSerializer(ctrl_pars, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ComusDisModel.DoesNotExist:
            return Response({'error': 'This COMUS model not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        user_name = request.data.get('user_name')
        project_name = request.data.get('project_name')
        comus_dis, _ = ComusDisModel.objects.get_or_create(user_name=user_name, project_name=project_name)
        request.data['comus_dis_uuid'] = comus_dis.uuid
        serializer = ComusOutParsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'COMUS output parameters saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user_name = request.data.get('user_name')
        project_name = request.data.get('project_name')

        try:
            comus_dis, _ = ComusDisModel.objects.get_or_create(user_name=user_name, project_name=project_name)
            request.data['comus_dis_uuid'] = comus_dis.uuid
        except ComusDisModel.DoesNotExist:
            return Response({'error': 'This COMUS model not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            ctrl_pars = ComusOutParsModel.objects.get(comus_dis_uuid=comus_dis.uuid)
        except ComusOutParsModel.DoesNotExist:
            return Response({'error': 'The output parameters of this COMUS model were not found!'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = ComusOutParsSerializer(ctrl_pars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'COMUS output parameters updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

