from django.db import models
import json
# Create your models here.
class Word(models.Model):
    eng = models.TextField(db_column="eng")
    ru = models.TextField(db_column="ru")
    eng_value = models.TextField(db_column="eng_value")
    def __str__(self):
        return '<Word: %s: %s-%s>' % (self.pk, self.eng, self.ru)
    def GetFields():
        return ["eng","ru","eng_value","id"]

#{
#	"#value": {
#		"Ref": "62209184-12cf-11eb-a204-7824af459690",
#		"DeletionMark": false,
#		"Code": "000000001",
#		"Description": "not use",
#		"ru": "рус",
#		"eng": "англ",
#		"eng_value": "знач"
#	}
#}
    def uploadJson(jsonStr):
        try:
            array=json.loads(jsonStr)
            for val in array:
                i=val["#value"]
                try:
                    Ref = RelateGuidId.objects.get(guid__exact=i["Ref"])
                except RelateGuidId.DoesNotExist:
                    w=Word()
                    w.eng=i["eng"]
                    w.ru=i["ru"]
                    w.eng_value=i["eng_value"]
                    w.save()

                    Ref=RelateGuidId()
                    Ref.guid=i["Ref"];
                    Ref.w=w
                    Ref.save()
                word=Ref.w;
                word.eng=i["eng"]
                word.ru=i["ru"]
                word.eng_value=i["eng_value"]
                word.save()
        except Exception as inst:
            return "Error:'"+str(inst)+"'." 
        return ""


class RelateGuidId(models.Model):
    guid = models.CharField(max_length=120,db_column="guid")
    w = models.ForeignKey(Word,db_column="w", on_delete=models.CASCADE)