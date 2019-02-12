from rest_framework.decorators import api_view
from story.models import Story
from .serializers import StorySerializer
from django.http import JsonResponse


@api_view(['GET', ])
def get_story_by_user(request, id=None):
    story = Story.objects.get(id=id)
    story_serializer = StorySerializer(story, many=True)
    response_json = {
        "story": story_serializer.data
    }
    return JsonResponse(response_json)
