from rest_framework import serializers
from .models import Resume, Jobexp, Project, Skill, Training, Education
import logging
from rest_framework.fields import IntegerField
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework.pagination import PageNumberPagination


class JobSerializer(serializers.ModelSerializer):
    # resume = serializers.IntegerField(read_only=True, source="Resume.id")
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Jobexp
        # fields = "__all__"
        exclude = ["resume"]


class ProjectSerializer(serializers.ModelSerializer):
    # resume = serializers.IntegerField(read_only=True, source="Resume.id")
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Project
        exclude = ["resume"]
        # fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    # resume = serializers.IntegerField(read_only=True, source="Resume.id")
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Skill
        exclude = ["resume"]
        # fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    # resume = serializers.IntegerField(read_only=True, source="Resume.id")
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Training
        exclude = ["resume"]
        # fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    # resume = serializers.IntegerField(read_only=True, source="Resume.id")
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Education
        exclude = ["resume"]
        # fields = "__all__"


def update_nest_obj(cls, validated_data, refname, ref):
    if "id" in validated_data:
        filter = {"pk": validated_data["id"], refname: ref}
        effortobject = cls.objects.filter(**filter).update(**validated_data)
        if not effortobject:
            raise serializers.ValidationError("not find object", 400)
    else:
        data = {refname: ref}
        data.update(validated_data)
        object = cls(**data)
        object.save()


class ResumeSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(many=True, required=False)
    projects = ProjectSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)
    trainings = TrainingSerializer(many=True, required=False)
    educations = EducationSerializer(many=True, required=False)

    class Meta:
        model = Resume
        fields = "__all__"

    def create(self, validated_data):
        jobs = validated_data.pop("jobs", [])
        projects = validated_data.pop("projects", [])
        skills = validated_data.pop("skills", [])
        trainings = validated_data.pop("trainings", [])
        educations = validated_data.pop("educations", [])

        resume = Resume.objects.create(**validated_data)
        for job in jobs:
            Jobexp.objects.create(resume=resume, **job)
        for project in projects:
            Project.objects.create(resume=resume, **project)
        for skill in skills:
            Skill.objects.create(resume=resume, **skill)
        for training in trainings:
            Training.objects.create(resume=resume, **training)
        for education in educations:
            Education.objects.create(resume=resume, **education)
        return resume

    def update(self, instance, validated_data):
        # Update the book instance
        jobs = validated_data.pop("jobs", [])
        projects = validated_data.pop("projects", [])
        skills = validated_data.pop("skills", [])
        trainings = validated_data.pop("trainings", [])
        educations = validated_data.pop("educations", [])

        for v in jobs:
            update_nest_obj(Jobexp, v, "resume", instance)

        for v in projects:
            update_nest_obj(Project, v, "resume", instance)

        for v in skills:
            update_nest_obj(Skill, v, "resume", instance)

        for v in trainings:
            update_nest_obj(Training, v, "resume", instance)

        for v in educations:
            update_nest_obj(Education, v, "resume", instance)

        instance.save()

        return instance


