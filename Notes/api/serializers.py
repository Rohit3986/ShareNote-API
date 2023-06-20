from rest_framework.serializers import ModelSerializer
from Notes.models import Note


class CreateNoteSerializer(ModelSerializer):
    
    class Meta:
        model = Note
        fields = ["id","note_type","text","file"]
        extra_kwargs = {'note_type':{'read_only':True},'user':{'read_only':True}}

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if data['file']:
            print(f"data is {data['file']}")
            extention = data['file'].name.rsplit('.')[-1]
            if extention in ['jpg','jpeg','png','svg']:
                data['note_type']="IMAGE"
            if extention in ['mp4','3gp','hevc']:
                data['note_type']="VIDEO"
            if extention in ['mp3','wav']:
                data['note_type']="AUDIO"   
            print(f'extenstion is {extention}')
        data['user'] = self.context['user']
        return data