from rest_framework import serializers


# Serializer to validate and deserialize input data for Parkinson's Disease prediction
class ParkinsonInputSerializer(serializers.Serializer):
    MDVP_Fo_Hz = serializers.FloatField()
    MDVP_Fhi_Hz = serializers.FloatField()
    MDVP_Flo_Hz = serializers.FloatField()
    MDVP_Jitter_percent = serializers.FloatField()
    MDVP_Jitter_Abs = serializers.FloatField()
    MDVP_RAP = serializers.FloatField()
    MDVP_PPQ = serializers.FloatField()
    Jitter_DDP = serializers.FloatField()
    MDVP_Shimmer = serializers.FloatField()
    MDVP_Shimmer_dB = serializers.FloatField()
    MDVP_APQ = serializers.FloatField()
    Shimmer_DDA = serializers.FloatField()
    NHR = serializers.FloatField()
    HNR = serializers.FloatField()
    RPDE = serializers.FloatField()
    DFA = serializers.FloatField()
    spread1 = serializers.FloatField()
    spread2 = serializers.FloatField()
    D2 = serializers.FloatField()
    PPE = serializers.FloatField()

    # Placeholder: Define additional validation rules here if needed
