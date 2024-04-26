"""PartStaticLoadAnalysisCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7571
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STATIC_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "PartStaticLoadAnalysisCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2708,
        _2709,
        _2710,
        _2713,
        _2714,
        _2715,
        _2721,
        _2723,
        _2725,
        _2726,
        _2727,
        _2728,
        _2730,
        _2731,
        _2732,
        _2733,
        _2735,
        _2736,
        _2738,
        _2741,
        _2742,
        _2744,
        _2745,
        _2748,
        _2749,
        _2751,
        _2753,
        _2754,
        _2756,
        _2757,
        _2758,
        _2761,
        _2765,
        _2766,
        _2767,
        _2768,
        _2769,
        _2770,
        _2773,
        _2774,
        _2775,
        _2778,
        _2779,
        _2780,
        _2781,
        _2783,
        _2784,
        _2785,
        _2787,
        _2788,
        _2792,
        _2793,
        _2795,
        _2796,
        _2798,
        _2799,
        _2802,
        _2803,
        _2805,
        _2807,
        _2808,
        _2810,
        _2811,
        _2813,
        _2814,
        _2815,
        _2816,
        _2817,
        _2820,
        _2822,
        _2823,
        _2824,
        _2827,
        _2829,
        _2831,
        _2832,
        _2834,
        _2835,
        _2837,
        _2838,
        _2840,
        _2841,
        _2842,
        _2843,
        _2844,
        _2845,
        _2846,
        _2847,
        _2852,
        _2853,
        _2854,
        _2857,
        _2858,
        _2860,
        _2861,
        _2863,
        _2864,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3006,
        _3007,
        _3008,
        _3011,
        _3012,
        _3013,
        _3014,
        _3016,
        _3018,
        _3019,
        _3020,
        _3021,
        _3023,
        _3024,
        _3025,
        _3026,
        _3028,
        _3029,
        _3031,
        _3033,
        _3034,
        _3036,
        _3037,
        _3039,
        _3040,
        _3042,
        _3044,
        _3045,
        _3047,
        _3048,
        _3049,
        _3052,
        _3054,
        _3055,
        _3056,
        _3057,
        _3059,
        _3061,
        _3062,
        _3063,
        _3064,
        _3066,
        _3067,
        _3068,
        _3070,
        _3071,
        _3074,
        _3075,
        _3077,
        _3078,
        _3080,
        _3081,
        _3082,
        _3083,
        _3084,
        _3085,
        _3086,
        _3088,
        _3089,
        _3091,
        _3092,
        _3093,
        _3094,
        _3095,
        _3096,
        _3098,
        _3100,
        _3101,
        _3102,
        _3103,
        _3105,
        _3107,
        _3108,
        _3110,
        _3111,
        _3116,
        _3117,
        _3119,
        _3120,
        _3121,
        _3122,
        _3123,
        _3124,
        _3125,
        _3126,
        _3128,
        _3129,
        _3130,
        _3131,
        _3132,
        _3134,
        _3135,
        _3137,
        _3138,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3268,
        _3269,
        _3270,
        _3273,
        _3274,
        _3275,
        _3276,
        _3278,
        _3280,
        _3281,
        _3282,
        _3283,
        _3285,
        _3286,
        _3287,
        _3288,
        _3290,
        _3291,
        _3293,
        _3295,
        _3296,
        _3298,
        _3299,
        _3301,
        _3302,
        _3304,
        _3306,
        _3307,
        _3309,
        _3310,
        _3311,
        _3314,
        _3316,
        _3317,
        _3318,
        _3319,
        _3320,
        _3322,
        _3323,
        _3324,
        _3325,
        _3327,
        _3328,
        _3329,
        _3331,
        _3332,
        _3335,
        _3336,
        _3338,
        _3339,
        _3341,
        _3342,
        _3343,
        _3344,
        _3345,
        _3346,
        _3347,
        _3349,
        _3350,
        _3352,
        _3353,
        _3354,
        _3355,
        _3356,
        _3357,
        _3359,
        _3361,
        _3362,
        _3363,
        _3364,
        _3366,
        _3368,
        _3369,
        _3371,
        _3372,
        _3375,
        _3376,
        _3378,
        _3379,
        _3380,
        _3381,
        _3382,
        _3383,
        _3384,
        _3385,
        _3387,
        _3388,
        _3389,
        _3390,
        _3391,
        _3393,
        _3394,
        _3396,
        _3397,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3527,
        _3528,
        _3529,
        _3532,
        _3533,
        _3534,
        _3535,
        _3537,
        _3539,
        _3540,
        _3541,
        _3542,
        _3544,
        _3545,
        _3546,
        _3547,
        _3549,
        _3550,
        _3552,
        _3554,
        _3555,
        _3557,
        _3558,
        _3560,
        _3561,
        _3563,
        _3565,
        _3566,
        _3568,
        _3569,
        _3570,
        _3573,
        _3575,
        _3576,
        _3577,
        _3578,
        _3579,
        _3581,
        _3582,
        _3583,
        _3584,
        _3586,
        _3587,
        _3588,
        _3590,
        _3591,
        _3594,
        _3595,
        _3597,
        _3598,
        _3600,
        _3601,
        _3602,
        _3603,
        _3604,
        _3605,
        _3606,
        _3608,
        _3609,
        _3611,
        _3612,
        _3613,
        _3614,
        _3615,
        _3616,
        _3618,
        _3620,
        _3621,
        _3622,
        _3623,
        _3625,
        _3627,
        _3628,
        _3630,
        _3631,
        _3634,
        _3635,
        _3637,
        _3638,
        _3639,
        _3640,
        _3641,
        _3642,
        _3643,
        _3644,
        _3646,
        _3647,
        _3648,
        _3649,
        _3650,
        _3652,
        _3653,
        _3655,
        _3656,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3786,
        _3787,
        _3788,
        _3791,
        _3792,
        _3793,
        _3794,
        _3796,
        _3798,
        _3799,
        _3800,
        _3801,
        _3803,
        _3804,
        _3805,
        _3806,
        _3808,
        _3809,
        _3811,
        _3813,
        _3814,
        _3816,
        _3817,
        _3819,
        _3820,
        _3822,
        _3824,
        _3825,
        _3828,
        _3829,
        _3830,
        _3833,
        _3835,
        _3836,
        _3837,
        _3838,
        _3840,
        _3842,
        _3843,
        _3844,
        _3845,
        _3847,
        _3848,
        _3849,
        _3851,
        _3852,
        _3855,
        _3856,
        _3858,
        _3859,
        _3861,
        _3862,
        _3863,
        _3864,
        _3865,
        _3866,
        _3867,
        _3869,
        _3870,
        _3872,
        _3873,
        _3874,
        _3875,
        _3876,
        _3877,
        _3879,
        _3881,
        _3882,
        _3883,
        _3884,
        _3886,
        _3888,
        _3889,
        _3891,
        _3892,
        _3897,
        _3898,
        _3900,
        _3901,
        _3902,
        _3903,
        _3904,
        _3905,
        _3906,
        _3907,
        _3909,
        _3910,
        _3911,
        _3912,
        _3913,
        _3915,
        _3916,
        _3918,
        _3919,
    )
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4055,
        _4056,
        _4057,
        _4060,
        _4061,
        _4062,
        _4063,
        _4065,
        _4067,
        _4068,
        _4069,
        _4070,
        _4072,
        _4073,
        _4074,
        _4075,
        _4077,
        _4078,
        _4080,
        _4082,
        _4083,
        _4085,
        _4086,
        _4088,
        _4089,
        _4091,
        _4093,
        _4094,
        _4096,
        _4097,
        _4098,
        _4101,
        _4104,
        _4105,
        _4106,
        _4107,
        _4108,
        _4110,
        _4111,
        _4114,
        _4115,
        _4117,
        _4118,
        _4119,
        _4121,
        _4122,
        _4125,
        _4126,
        _4128,
        _4129,
        _4131,
        _4132,
        _4133,
        _4134,
        _4135,
        _4136,
        _4137,
        _4139,
        _4140,
        _4142,
        _4143,
        _4144,
        _4147,
        _4148,
        _4149,
        _4151,
        _4153,
        _4154,
        _4155,
        _4156,
        _4158,
        _4160,
        _4161,
        _4163,
        _4164,
        _4166,
        _4167,
        _4169,
        _4170,
        _4171,
        _4172,
        _4173,
        _4174,
        _4175,
        _4176,
        _4179,
        _4180,
        _4181,
        _4182,
        _4183,
        _4185,
        _4186,
        _4188,
        _4189,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4595,
        _4596,
        _4597,
        _4600,
        _4601,
        _4602,
        _4603,
        _4605,
        _4607,
        _4608,
        _4609,
        _4610,
        _4612,
        _4613,
        _4614,
        _4615,
        _4617,
        _4618,
        _4620,
        _4622,
        _4623,
        _4625,
        _4626,
        _4628,
        _4629,
        _4631,
        _4634,
        _4635,
        _4637,
        _4638,
        _4639,
        _4641,
        _4644,
        _4645,
        _4646,
        _4647,
        _4651,
        _4653,
        _4654,
        _4655,
        _4656,
        _4659,
        _4660,
        _4661,
        _4663,
        _4664,
        _4667,
        _4668,
        _4670,
        _4671,
        _4673,
        _4674,
        _4675,
        _4676,
        _4681,
        _4683,
        _4685,
        _4687,
        _4688,
        _4690,
        _4691,
        _4692,
        _4693,
        _4694,
        _4695,
        _4697,
        _4699,
        _4700,
        _4701,
        _4702,
        _4705,
        _4707,
        _4708,
        _4710,
        _4711,
        _4713,
        _4714,
        _4716,
        _4717,
        _4718,
        _4719,
        _4720,
        _4721,
        _4722,
        _4723,
        _4725,
        _4726,
        _4727,
        _4728,
        _4729,
        _4734,
        _4735,
        _4737,
        _4738,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4880,
        _4881,
        _4882,
        _4885,
        _4886,
        _4887,
        _4888,
        _4890,
        _4892,
        _4893,
        _4894,
        _4895,
        _4897,
        _4898,
        _4899,
        _4900,
        _4902,
        _4903,
        _4905,
        _4907,
        _4908,
        _4910,
        _4911,
        _4913,
        _4914,
        _4916,
        _4918,
        _4919,
        _4921,
        _4922,
        _4923,
        _4925,
        _4928,
        _4929,
        _4930,
        _4931,
        _4933,
        _4935,
        _4936,
        _4937,
        _4938,
        _4940,
        _4941,
        _4942,
        _4944,
        _4945,
        _4948,
        _4949,
        _4951,
        _4952,
        _4954,
        _4955,
        _4956,
        _4957,
        _4959,
        _4960,
        _4961,
        _4963,
        _4964,
        _4966,
        _4967,
        _4968,
        _4969,
        _4970,
        _4971,
        _4973,
        _4975,
        _4976,
        _4977,
        _4978,
        _4980,
        _4982,
        _4983,
        _4985,
        _4986,
        _4988,
        _4989,
        _4991,
        _4992,
        _4993,
        _4994,
        _4995,
        _4996,
        _4997,
        _4998,
        _5000,
        _5001,
        _5002,
        _5003,
        _5004,
        _5006,
        _5007,
        _5009,
        _5010,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5140,
        _5141,
        _5142,
        _5145,
        _5146,
        _5147,
        _5148,
        _5150,
        _5152,
        _5153,
        _5154,
        _5155,
        _5157,
        _5158,
        _5159,
        _5160,
        _5162,
        _5163,
        _5165,
        _5167,
        _5168,
        _5170,
        _5171,
        _5173,
        _5174,
        _5176,
        _5178,
        _5179,
        _5181,
        _5182,
        _5183,
        _5185,
        _5188,
        _5189,
        _5190,
        _5191,
        _5192,
        _5194,
        _5195,
        _5196,
        _5197,
        _5199,
        _5200,
        _5201,
        _5203,
        _5204,
        _5207,
        _5208,
        _5210,
        _5211,
        _5213,
        _5214,
        _5215,
        _5216,
        _5218,
        _5219,
        _5220,
        _5222,
        _5223,
        _5225,
        _5226,
        _5227,
        _5228,
        _5229,
        _5230,
        _5232,
        _5234,
        _5235,
        _5236,
        _5237,
        _5239,
        _5241,
        _5242,
        _5244,
        _5245,
        _5247,
        _5248,
        _5250,
        _5251,
        _5252,
        _5253,
        _5254,
        _5255,
        _5256,
        _5257,
        _5259,
        _5260,
        _5261,
        _5262,
        _5263,
        _5265,
        _5266,
        _5268,
        _5269,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5704,
        _5706,
        _5707,
        _5709,
        _5711,
        _5712,
        _5713,
        _5715,
        _5716,
        _5718,
        _5719,
        _5720,
        _5721,
        _5723,
        _5724,
        _5725,
        _5727,
        _5728,
        _5731,
        _5733,
        _5734,
        _5735,
        _5737,
        _5738,
        _5740,
        _5742,
        _5744,
        _5745,
        _5747,
        _5748,
        _5749,
        _5751,
        _5753,
        _5755,
        _5756,
        _5757,
        _5772,
        _5773,
        _5775,
        _5776,
        _5777,
        _5779,
        _5784,
        _5786,
        _5797,
        _5799,
        _5801,
        _5803,
        _5804,
        _5806,
        _5807,
        _5809,
        _5810,
        _5811,
        _5812,
        _5813,
        _5814,
        _5816,
        _5817,
        _5820,
        _5821,
        _5822,
        _5823,
        _5824,
        _5826,
        _5828,
        _5830,
        _5831,
        _5832,
        _5833,
        _5836,
        _5838,
        _5840,
        _5842,
        _5843,
        _5845,
        _5847,
        _5848,
        _5850,
        _5851,
        _5852,
        _5853,
        _5854,
        _5855,
        _5856,
        _5858,
        _5859,
        _5860,
        _5862,
        _5863,
        _5864,
        _5866,
        _5867,
        _5869,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6034,
        _6035,
        _6036,
        _6038,
        _6040,
        _6041,
        _6042,
        _6044,
        _6045,
        _6047,
        _6048,
        _6049,
        _6050,
        _6052,
        _6053,
        _6054,
        _6056,
        _6057,
        _6059,
        _6061,
        _6062,
        _6063,
        _6065,
        _6066,
        _6068,
        _6070,
        _6072,
        _6073,
        _6075,
        _6076,
        _6077,
        _6079,
        _6081,
        _6083,
        _6084,
        _6085,
        _6086,
        _6087,
        _6089,
        _6090,
        _6091,
        _6092,
        _6094,
        _6095,
        _6097,
        _6099,
        _6101,
        _6103,
        _6104,
        _6106,
        _6107,
        _6109,
        _6110,
        _6111,
        _6113,
        _6114,
        _6115,
        _6117,
        _6118,
        _6120,
        _6121,
        _6122,
        _6123,
        _6124,
        _6125,
        _6127,
        _6129,
        _6130,
        _6131,
        _6132,
        _6134,
        _6135,
        _6137,
        _6139,
        _6140,
        _6141,
        _6143,
        _6144,
        _6146,
        _6147,
        _6148,
        _6149,
        _6150,
        _6151,
        _6152,
        _6154,
        _6155,
        _6156,
        _6157,
        _6158,
        _6159,
        _6161,
        _6162,
        _6164,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6303,
        _6304,
        _6305,
        _6307,
        _6309,
        _6310,
        _6311,
        _6313,
        _6314,
        _6316,
        _6317,
        _6318,
        _6319,
        _6321,
        _6322,
        _6323,
        _6325,
        _6326,
        _6328,
        _6330,
        _6331,
        _6332,
        _6334,
        _6335,
        _6337,
        _6339,
        _6341,
        _6342,
        _6344,
        _6345,
        _6346,
        _6348,
        _6350,
        _6352,
        _6353,
        _6354,
        _6357,
        _6358,
        _6360,
        _6361,
        _6362,
        _6363,
        _6365,
        _6366,
        _6367,
        _6369,
        _6371,
        _6373,
        _6374,
        _6376,
        _6377,
        _6379,
        _6380,
        _6381,
        _6382,
        _6383,
        _6384,
        _6386,
        _6387,
        _6389,
        _6390,
        _6391,
        _6392,
        _6393,
        _6394,
        _6396,
        _6398,
        _6399,
        _6400,
        _6401,
        _6403,
        _6404,
        _6406,
        _6408,
        _6409,
        _6410,
        _6412,
        _6413,
        _6415,
        _6416,
        _6417,
        _6418,
        _6419,
        _6420,
        _6421,
        _6423,
        _6424,
        _6425,
        _6426,
        _6427,
        _6428,
        _6430,
        _6431,
        _6433,
    )
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6569,
        _6570,
        _6571,
        _6573,
        _6575,
        _6576,
        _6577,
        _6579,
        _6580,
        _6582,
        _6583,
        _6584,
        _6585,
        _6587,
        _6588,
        _6589,
        _6591,
        _6592,
        _6594,
        _6596,
        _6597,
        _6598,
        _6600,
        _6601,
        _6603,
        _6605,
        _6607,
        _6608,
        _6613,
        _6614,
        _6615,
        _6617,
        _6619,
        _6621,
        _6622,
        _6623,
        _6624,
        _6625,
        _6627,
        _6628,
        _6629,
        _6630,
        _6632,
        _6633,
        _6634,
        _6636,
        _6638,
        _6640,
        _6641,
        _6643,
        _6644,
        _6646,
        _6647,
        _6648,
        _6649,
        _6650,
        _6651,
        _6653,
        _6654,
        _6656,
        _6657,
        _6658,
        _6659,
        _6660,
        _6661,
        _6663,
        _6665,
        _6666,
        _6667,
        _6668,
        _6670,
        _6671,
        _6673,
        _6675,
        _6676,
        _6677,
        _6679,
        _6680,
        _6682,
        _6683,
        _6684,
        _6685,
        _6686,
        _6687,
        _6688,
        _6690,
        _6691,
        _6692,
        _6693,
        _6694,
        _6695,
        _6697,
        _6698,
        _6700,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7032,
        _7033,
        _7034,
        _7040,
        _7042,
        _7043,
        _7045,
        _7047,
        _7048,
        _7050,
        _7051,
        _7052,
        _7053,
        _7055,
        _7056,
        _7057,
        _7058,
        _7060,
        _7062,
        _7063,
        _7065,
        _7066,
        _7068,
        _7069,
        _7071,
        _7073,
        _7074,
        _7076,
        _7077,
        _7079,
        _7080,
        _7081,
        _7084,
        _7086,
        _7087,
        _7088,
        _7089,
        _7090,
        _7092,
        _7093,
        _7094,
        _7095,
        _7097,
        _7098,
        _7100,
        _7102,
        _7104,
        _7106,
        _7107,
        _7109,
        _7110,
        _7112,
        _7113,
        _7114,
        _7115,
        _7116,
        _7117,
        _7118,
        _7120,
        _7122,
        _7123,
        _7124,
        _7125,
        _7126,
        _7127,
        _7129,
        _7130,
        _7132,
        _7133,
        _7134,
        _7136,
        _7137,
        _7139,
        _7140,
        _7142,
        _7143,
        _7145,
        _7146,
        _7148,
        _7149,
        _7150,
        _7151,
        _7152,
        _7153,
        _7154,
        _7155,
        _7157,
        _7158,
        _7159,
        _7160,
        _7161,
        _7163,
        _7164,
        _7166,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7296,
        _7297,
        _7298,
        _7303,
        _7305,
        _7306,
        _7307,
        _7309,
        _7310,
        _7312,
        _7313,
        _7314,
        _7315,
        _7317,
        _7318,
        _7319,
        _7320,
        _7322,
        _7324,
        _7325,
        _7327,
        _7328,
        _7330,
        _7331,
        _7333,
        _7335,
        _7337,
        _7339,
        _7340,
        _7342,
        _7343,
        _7344,
        _7347,
        _7349,
        _7351,
        _7352,
        _7353,
        _7354,
        _7356,
        _7357,
        _7358,
        _7359,
        _7361,
        _7362,
        _7363,
        _7365,
        _7367,
        _7369,
        _7370,
        _7372,
        _7373,
        _7375,
        _7377,
        _7378,
        _7379,
        _7380,
        _7381,
        _7382,
        _7384,
        _7386,
        _7387,
        _7388,
        _7389,
        _7390,
        _7391,
        _7393,
        _7394,
        _7396,
        _7397,
        _7398,
        _7400,
        _7401,
        _7403,
        _7404,
        _7406,
        _7407,
        _7409,
        _7410,
        _7412,
        _7413,
        _7414,
        _7415,
        _7416,
        _7417,
        _7418,
        _7419,
        _7421,
        _7422,
        _7424,
        _7425,
        _7426,
        _7428,
        _7429,
        _7431,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7573
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartStaticLoadAnalysisCase",)


Self = TypeVar("Self", bound="PartStaticLoadAnalysisCase")


class PartStaticLoadAnalysisCase(_7571.PartAnalysisCase):
    """PartStaticLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _PART_STATIC_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartStaticLoadAnalysisCase")

    class _Cast_PartStaticLoadAnalysisCase:
        """Special nested class for casting PartStaticLoadAnalysisCase to subclasses."""

        def __init__(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
            parent: "PartStaticLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def part_analysis_case(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7571.PartAnalysisCase":
            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2708.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2709.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2710.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2713.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2714.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2715.AssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2721.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2723.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2725.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2726.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2727.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2728.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2730.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2731.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2732.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2733.BoltSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2735.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2736.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2741.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2742.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2744.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2745.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2748.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2749.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2751.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2751,
            )

            return self._parent._cast(_2751.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2753.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2754.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2756.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2757.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2758.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2761.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2765.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2766.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2767.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2768.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(_2768.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2769.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(_2769.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2770.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2773.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2774.DatumSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(_2774.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2775.ExternalCADModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(_2775.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2778.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2779.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2780.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2781.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2783.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2784.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2785.GuideDxfModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2787.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2788.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(
                _2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2793.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(
                _2793.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(
                _2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(
                _2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(
                _2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2799.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(
                _2799.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2802.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2803.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2807.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.OilSealSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2810.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2811.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2813.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2814.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2815.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2816.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2817.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2820.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2822.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2823.RootAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2824.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2827.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2831.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2832.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2834.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2835.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2837.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2838.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2840.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2841.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2842.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2843.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2844.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2844,
            )

            return self._parent._cast(_2844.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2845.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2845,
            )

            return self._parent._cast(_2845.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2846.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2847.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2847,
            )

            return self._parent._cast(_2847.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2852.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2852,
            )

            return self._parent._cast(_2852.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2853.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2853,
            )

            return self._parent._cast(_2853.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2854.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2854,
            )

            return self._parent._cast(_2854.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2857.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2857,
            )

            return self._parent._cast(_2857.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2858.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2858,
            )

            return self._parent._cast(_2858.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2860.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2860,
            )

            return self._parent._cast(_2860.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2861.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2861,
            )

            return self._parent._cast(_2861.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2863.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2863,
            )

            return self._parent._cast(_2863.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_2864.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2864,
            )

            return self._parent._cast(_2864.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3006.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3007.AbstractShaftOrHousingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(
                _3007.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3008.AbstractShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3008,
            )

            return self._parent._cast(_3008.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3011.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(
                _3011.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3012.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3013.AssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(_3013.AssemblySteadyStateSynchronousResponse)

        @property
        def bearing_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3014.BearingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.BearingSteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3016.BeltDriveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3018.BevelDifferentialGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3019.BevelDifferentialGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(
                _3019.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3020.BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(
                _3020.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3021.BevelDifferentialSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(
                _3021.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3023.BevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(_3023.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3024.BevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(_3024.BevelGearSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3025.BoltedJointSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(_3025.BoltedJointSteadyStateSynchronousResponse)

        @property
        def bolt_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3026.BoltSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.BoltSteadyStateSynchronousResponse)

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3028.ClutchHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3028,
            )

            return self._parent._cast(_3028.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3029.ClutchSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ClutchSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3033.ConceptCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3033,
            )

            return self._parent._cast(
                _3033.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3034.ConceptCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3034,
            )

            return self._parent._cast(
                _3034.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3036.ConceptGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3036,
            )

            return self._parent._cast(
                _3036.ConceptGearSetSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3037.ConceptGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3037,
            )

            return self._parent._cast(_3037.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3039.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(
                _3039.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3040.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.ConicalGearSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3042.ConnectorSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.ConnectorSteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3044.CouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(_3044.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def coupling_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3045.CouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3047.CVTPulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(_3047.CVTPulleySteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3048.CVTSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(_3048.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3049.CycloidalAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3049,
            )

            return self._parent._cast(
                _3049.CycloidalAssemblySteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3052.CycloidalDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(_3052.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3054.CylindricalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3055.CylindricalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(
                _3055.CylindricalGearSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3056.CylindricalPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(
                _3056.CylindricalPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def datum_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3057.DatumSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(_3057.DatumSteadyStateSynchronousResponse)

        @property
        def external_cad_model_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3059.ExternalCADModelSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(
                _3059.ExternalCADModelSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3061.FaceGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def face_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3062.FaceGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(_3062.FaceGearSteadyStateSynchronousResponse)

        @property
        def fe_part_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3063.FEPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.FEPartSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3064.FlexiblePinAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.FlexiblePinAssemblySteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3066.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(_3066.GearSetSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3067.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3067,
            )

            return self._parent._cast(_3067.GearSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3068.GuideDxfModelSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(_3068.GuideDxfModelSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3070.HypoidGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3070,
            )

            return self._parent._cast(_3070.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3071.HypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> (
            "_3074.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(
                _3074.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3075.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(
                _3075.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> (
            "_3077.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3077,
            )

            return self._parent._cast(
                _3077.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3078.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3078,
            )

            return self._parent._cast(
                _3078.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3080.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3080,
            )

            return self._parent._cast(
                _3080.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3081.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3082.MassDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(_3082.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3083.MeasurementComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3083,
            )

            return self._parent._cast(
                _3083.MeasurementComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3084.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3085.OilSealSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3085,
            )

            return self._parent._cast(_3085.OilSealSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3088.PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3088,
            )

            return self._parent._cast(
                _3088.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3089.PartToPartShearCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3089,
            )

            return self._parent._cast(
                _3089.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3091.PlanetaryGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3091,
            )

            return self._parent._cast(
                _3091.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3092.PlanetCarrierSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3092,
            )

            return self._parent._cast(_3092.PlanetCarrierSteadyStateSynchronousResponse)

        @property
        def point_load_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3093.PointLoadSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(_3093.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3094.PowerLoadSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(_3094.PowerLoadSteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3095.PulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3095,
            )

            return self._parent._cast(_3095.PulleySteadyStateSynchronousResponse)

        @property
        def ring_pins_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3096.RingPinsSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(_3096.RingPinsSteadyStateSynchronousResponse)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3098.RollingRingAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3098,
            )

            return self._parent._cast(
                _3098.RollingRingAssemblySteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3100.RollingRingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(_3100.RollingRingSteadyStateSynchronousResponse)

        @property
        def root_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3101.RootAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3101,
            )

            return self._parent._cast(_3101.RootAssemblySteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3102.ShaftHubConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.ShaftHubConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3103.ShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(_3103.ShaftSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3105.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3107.SpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3107,
            )

            return self._parent._cast(
                _3107.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3108.SpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(
                _3108.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3110.SpringDamperHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(
                _3110.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3111.SpringDamperSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(_3111.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3116.StraightBevelDiffGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3116,
            )

            return self._parent._cast(
                _3116.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3117.StraightBevelDiffGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3117,
            )

            return self._parent._cast(
                _3117.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3119.StraightBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3119,
            )

            return self._parent._cast(
                _3119.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3120.StraightBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3120,
            )

            return self._parent._cast(
                _3120.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3121.StraightBevelPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3121,
            )

            return self._parent._cast(
                _3121.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3122.StraightBevelSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3122,
            )

            return self._parent._cast(
                _3122.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3123.SynchroniserHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3123,
            )

            return self._parent._cast(
                _3123.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3124.SynchroniserPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3124,
            )

            return self._parent._cast(
                _3124.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3125.SynchroniserSleeveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3125,
            )

            return self._parent._cast(
                _3125.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3126.SynchroniserSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3126,
            )

            return self._parent._cast(_3126.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3128.TorqueConverterPumpSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3128,
            )

            return self._parent._cast(
                _3128.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3129.TorqueConverterSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3129,
            )

            return self._parent._cast(
                _3129.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3130.TorqueConverterTurbineSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3130,
            )

            return self._parent._cast(
                _3130.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3131.UnbalancedMassSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3131,
            )

            return self._parent._cast(
                _3131.UnbalancedMassSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3132.VirtualComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3132,
            )

            return self._parent._cast(
                _3132.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3134.WormGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3134,
            )

            return self._parent._cast(_3134.WormGearSetSteadyStateSynchronousResponse)

        @property
        def worm_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3135.WormGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3135,
            )

            return self._parent._cast(_3135.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3137.ZerolBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3137,
            )

            return self._parent._cast(
                _3137.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3138.ZerolBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3138,
            )

            return self._parent._cast(
                _3138.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3269.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3269,
            )

            return self._parent._cast(
                _3269.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3270.AbstractShaftSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.AbstractShaftSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3273.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3274.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3274,
            )

            return self._parent._cast(
                _3274.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3275.AssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3275,
            )

            return self._parent._cast(
                _3275.AssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3276.BearingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3276,
            )

            return self._parent._cast(
                _3276.BearingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3278.BeltDriveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3280.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3281.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3281,
            )

            return self._parent._cast(
                _3281.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3282.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3283.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3283,
            )

            return self._parent._cast(
                _3283.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3285.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(
                _3285.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3286.BevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3286,
            )

            return self._parent._cast(
                _3286.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3287.BoltedJointSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(
                _3287.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3288.BoltSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(_3288.BoltSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3290.ClutchHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3290,
            )

            return self._parent._cast(
                _3290.ClutchHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3291.ClutchSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3293.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3295.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3295,
            )

            return self._parent._cast(
                _3295.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3296.ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3296,
            )

            return self._parent._cast(
                _3296.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3298.ConceptGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3298,
            )

            return self._parent._cast(
                _3298.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3299.ConceptGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.ConceptGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3301.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3302.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3304.ConnectorSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3304,
            )

            return self._parent._cast(
                _3304.ConnectorSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3306.CouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3306,
            )

            return self._parent._cast(
                _3306.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3307.CouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(
                _3307.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3309.CVTPulleySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.CVTPulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3310.CVTSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(_3310.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3311.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3311,
            )

            return self._parent._cast(
                _3311.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3314.CycloidalDiscSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3314,
            )

            return self._parent._cast(
                _3314.CycloidalDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3316.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3316,
            )

            return self._parent._cast(
                _3316.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3317.CylindricalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3317,
            )

            return self._parent._cast(
                _3317.CylindricalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3318.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3319.DatumSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(_3319.DatumSteadyStateSynchronousResponseOnAShaft)

        @property
        def external_cad_model_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3320.ExternalCADModelSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3320,
            )

            return self._parent._cast(
                _3320.ExternalCADModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3322.FaceGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3323.FaceGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3323,
            )

            return self._parent._cast(
                _3323.FaceGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3324.FEPartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.FEPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3325.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3327.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3328.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3328,
            )

            return self._parent._cast(_3328.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def guide_dxf_model_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3329.GuideDxfModelSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3329,
            )

            return self._parent._cast(
                _3329.GuideDxfModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3331.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3332.HypoidGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(
                _3332.HypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3335.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3335,
            )

            return self._parent._cast(
                _3335.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3336.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3336,
            )

            return self._parent._cast(
                _3336.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3338.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3338,
            )

            return self._parent._cast(
                _3338.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3339.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3339,
            )

            return self._parent._cast(
                _3339.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3341.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3342.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3342,
            )

            return self._parent._cast(
                _3342.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3343.MassDiscSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.MassDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3344.MeasurementComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3344,
            )

            return self._parent._cast(
                _3344.MeasurementComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3345.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3346.OilSealSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.OilSealSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3349.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3350.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3350,
            )

            return self._parent._cast(
                _3350.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3352.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3353.PlanetCarrierSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.PlanetCarrierSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3354.PointLoadSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3354,
            )

            return self._parent._cast(
                _3354.PointLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3355.PowerLoadSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3355,
            )

            return self._parent._cast(
                _3355.PowerLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3356.PulleySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3356,
            )

            return self._parent._cast(
                _3356.PulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3357.RingPinsSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3357,
            )

            return self._parent._cast(
                _3357.RingPinsSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3359.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3361.RollingRingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3361,
            )

            return self._parent._cast(
                _3361.RollingRingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3362.RootAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.RootAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3363.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3363,
            )

            return self._parent._cast(
                _3363.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3364.ShaftSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3364,
            )

            return self._parent._cast(_3364.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3368.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3368,
            )

            return self._parent._cast(
                _3368.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3369.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3369,
            )

            return self._parent._cast(
                _3369.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3371.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3371,
            )

            return self._parent._cast(
                _3371.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3372.SpringDamperSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3372,
            )

            return self._parent._cast(
                _3372.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3375.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3375,
            )

            return self._parent._cast(
                _3375.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3376.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3376,
            )

            return self._parent._cast(
                _3376.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3378.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3378,
            )

            return self._parent._cast(
                _3378.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3379.StraightBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3379,
            )

            return self._parent._cast(
                _3379.StraightBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3380.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3380,
            )

            return self._parent._cast(
                _3380.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3381.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3381,
            )

            return self._parent._cast(
                _3381.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3382.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3382,
            )

            return self._parent._cast(
                _3382.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3383.SynchroniserPartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3383,
            )

            return self._parent._cast(
                _3383.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3384.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3384,
            )

            return self._parent._cast(
                _3384.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3385.SynchroniserSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3385,
            )

            return self._parent._cast(
                _3385.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3387.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3387,
            )

            return self._parent._cast(
                _3387.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3388.TorqueConverterSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3388,
            )

            return self._parent._cast(
                _3388.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3389.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3389,
            )

            return self._parent._cast(
                _3389.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3390.UnbalancedMassSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3390,
            )

            return self._parent._cast(
                _3390.UnbalancedMassSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3391.VirtualComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3391,
            )

            return self._parent._cast(
                _3391.VirtualComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3393.WormGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3393,
            )

            return self._parent._cast(
                _3393.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3394.WormGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3394,
            )

            return self._parent._cast(
                _3394.WormGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3396.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3396,
            )

            return self._parent._cast(
                _3396.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3397.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3397,
            )

            return self._parent._cast(
                _3397.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3527.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3528.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3529.AbstractShaftSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3532.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3532,
            )

            return self._parent._cast(
                _3532.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3533.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3534.AssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.AssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3535.BearingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3537.BeltDriveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3539.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3540.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3541.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3541,
            )

            return self._parent._cast(
                _3541.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3542.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3544.BevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3544,
            )

            return self._parent._cast(
                _3544.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3545.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3545,
            )

            return self._parent._cast(
                _3545.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3546.BoltedJointSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3546,
            )

            return self._parent._cast(
                _3546.BoltedJointSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3547.BoltSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(_3547.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3549.ClutchHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3549,
            )

            return self._parent._cast(
                _3549.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3550.ClutchSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3552.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3554.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3554,
            )

            return self._parent._cast(
                _3554.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3555.ConceptCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3557.ConceptGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3557,
            )

            return self._parent._cast(
                _3557.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3558.ConceptGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3558,
            )

            return self._parent._cast(
                _3558.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3560.ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3561.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3563.ConnectorSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3563,
            )

            return self._parent._cast(
                _3563.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3566.CouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3568.CVTPulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3569.CVTSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(_3569.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3570.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3570,
            )

            return self._parent._cast(
                _3570.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3573.CycloidalDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3573,
            )

            return self._parent._cast(
                _3573.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3575.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3576.CylindricalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3577.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3578.DatumSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(_3578.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3579.ExternalCADModelSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.ExternalCADModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3581.FaceGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(
                _3581.FaceGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3582.FaceGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3583.FEPartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.FEPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3584.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3584,
            )

            return self._parent._cast(
                _3584.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3586.GearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3586,
            )

            return self._parent._cast(
                _3586.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3587.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(_3587.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3588.GuideDxfModelSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.GuideDxfModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3590.HypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3591.HypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(
                _3591.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3594.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3595.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3595,
            )

            return self._parent._cast(
                _3595.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3597.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3597,
            )

            return self._parent._cast(
                _3597.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3598.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3598,
            )

            return self._parent._cast(
                _3598.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3600.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3601.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3602.MassDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3603.MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3604.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3605.OilSealSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3605,
            )

            return self._parent._cast(
                _3605.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3608.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3609.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(
                _3609.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3611.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3612.PlanetCarrierSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3613.PointLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3614.PowerLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3615.PulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3616.RingPinsSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3618.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3618,
            )

            return self._parent._cast(
                _3618.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3620.RollingRingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3621.RootAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3621,
            )

            return self._parent._cast(
                _3621.RootAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3622.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3623.ShaftSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(_3623.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3625.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3625,
            )

            return self._parent._cast(
                _3625.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3627.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3627,
            )

            return self._parent._cast(
                _3627.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3628.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3628,
            )

            return self._parent._cast(
                _3628.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3630.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(
                _3630.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3631.SpringDamperSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3631,
            )

            return self._parent._cast(
                _3631.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3634.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3634,
            )

            return self._parent._cast(
                _3634.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3635.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3635,
            )

            return self._parent._cast(
                _3635.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3637.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3637,
            )

            return self._parent._cast(
                _3637.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3638.StraightBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3638,
            )

            return self._parent._cast(
                _3638.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3639.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3639,
            )

            return self._parent._cast(
                _3639.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3640.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3640,
            )

            return self._parent._cast(
                _3640.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3641.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3641,
            )

            return self._parent._cast(
                _3641.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3642.SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3642,
            )

            return self._parent._cast(
                _3642.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3643.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3643,
            )

            return self._parent._cast(
                _3643.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3644.SynchroniserSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3644,
            )

            return self._parent._cast(
                _3644.SynchroniserSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3646.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3646,
            )

            return self._parent._cast(
                _3646.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3647.TorqueConverterSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3647,
            )

            return self._parent._cast(
                _3647.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3648.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3648,
            )

            return self._parent._cast(
                _3648.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3649.UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3649,
            )

            return self._parent._cast(
                _3649.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3650.VirtualComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3650,
            )

            return self._parent._cast(
                _3650.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3652.WormGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3652,
            )

            return self._parent._cast(
                _3652.WormGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3653.WormGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3653,
            )

            return self._parent._cast(
                _3653.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3655.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3655,
            )

            return self._parent._cast(
                _3655.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3656.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3656,
            )

            return self._parent._cast(
                _3656.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3786.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.AbstractAssemblyStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3787.AbstractShaftOrHousingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3788.AbstractShaftStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.AbstractShaftStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3791.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3792.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3793.AssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.AssemblyStabilityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3794.BearingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.BearingStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3796.BeltDriveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3798.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3799.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3800.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(
                _3800.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3801.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3801,
            )

            return self._parent._cast(_3801.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3803.BevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.BevelGearSetStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3804.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.BevelGearStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3805.BoltedJointStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3805,
            )

            return self._parent._cast(_3805.BoltedJointStabilityAnalysis)

        @property
        def bolt_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3806.BoltStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.BoltStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3808.ClutchHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.ClutchHalfStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3809.ClutchStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ClutchStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3813.ConceptCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3814.ConceptCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3816.ConceptGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.ConceptGearSetStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3817.ConceptGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3819.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3820.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3822.ConnectorStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3824.CouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3824,
            )

            return self._parent._cast(_3824.CouplingHalfStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3825.CouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.CouplingStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3828.CVTPulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(_3828.CVTPulleyStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3829.CVTStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(_3829.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3830.CycloidalAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(_3830.CycloidalAssemblyStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3833.CycloidalDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(_3833.CycloidalDiscStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3835.CylindricalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(_3835.CylindricalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3836.CylindricalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(_3836.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3837.CylindricalPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.CylindricalPlanetGearStabilityAnalysis)

        @property
        def datum_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3838.DatumStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(_3838.DatumStabilityAnalysis)

        @property
        def external_cad_model_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3840.ExternalCADModelStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.ExternalCADModelStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3842.FaceGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.FaceGearSetStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3843.FaceGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(_3843.FaceGearStabilityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3844.FEPartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.FEPartStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3845.FlexiblePinAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3847.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.GearSetStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3848.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.GearStabilityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3849.GuideDxfModelStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.GuideDxfModelStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3851.HypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.HypoidGearSetStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3852.HypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3855.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(
                _3855.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3856.KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(
                _3856.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3858.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(
                _3858.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3859.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(
                _3859.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3861.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(
                _3861.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3862.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(
                _3862.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3863.MassDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3864.MeasurementComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.MeasurementComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3866.OilSealStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.OilSealStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3869.PartToPartShearCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3869,
            )

            return self._parent._cast(
                _3869.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3870.PartToPartShearCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3870,
            )

            return self._parent._cast(_3870.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3872.PlanetaryGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.PlanetaryGearSetStabilityAnalysis)

        @property
        def planet_carrier_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3873.PlanetCarrierStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3874.PointLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3875.PowerLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3876.PulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3877.RingPinsStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3879.RollingRingAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.RollingRingAssemblyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3881.RollingRingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.RollingRingStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3882.RootAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.RootAssemblyStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3883.ShaftHubConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.ShaftHubConnectionStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3884.ShaftStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.ShaftStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3886.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3888.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3889.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3891.SpringDamperHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3891,
            )

            return self._parent._cast(_3891.SpringDamperHalfStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3892.SpringDamperStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3897.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3898.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3898,
            )

            return self._parent._cast(_3898.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3900.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3900,
            )

            return self._parent._cast(_3900.StraightBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3901.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3901,
            )

            return self._parent._cast(_3901.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3902.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3902,
            )

            return self._parent._cast(_3902.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3903.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3903,
            )

            return self._parent._cast(_3903.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3904.SynchroniserHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3904,
            )

            return self._parent._cast(_3904.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3905.SynchroniserPartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3905,
            )

            return self._parent._cast(_3905.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3906.SynchroniserSleeveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3906,
            )

            return self._parent._cast(_3906.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3907.SynchroniserStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3907,
            )

            return self._parent._cast(_3907.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3909.TorqueConverterPumpStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3909,
            )

            return self._parent._cast(_3909.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3910.TorqueConverterStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3910,
            )

            return self._parent._cast(_3910.TorqueConverterStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3911.TorqueConverterTurbineStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3911,
            )

            return self._parent._cast(_3911.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3912.UnbalancedMassStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3912,
            )

            return self._parent._cast(_3912.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3913.VirtualComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3913,
            )

            return self._parent._cast(_3913.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3915.WormGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3915,
            )

            return self._parent._cast(_3915.WormGearSetStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3916.WormGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3916,
            )

            return self._parent._cast(_3916.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3918.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3918,
            )

            return self._parent._cast(_3918.ZerolBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_3919.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3919,
            )

            return self._parent._cast(_3919.ZerolBevelGearStabilityAnalysis)

        @property
        def abstract_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4056.AbstractShaftOrHousingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(_4056.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4057.AbstractShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4060.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4061.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4062.AssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.AssemblyPowerFlow)

        @property
        def bearing_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4063.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.BearingPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4065.BeltDrivePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4067.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4068.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4069.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4070.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4072.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4073.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4074.BoltedJointPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4075.BoltPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.BoltPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4077.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4077

            return self._parent._cast(_4077.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4078.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ClutchPowerFlow)

        @property
        def component_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4082.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4083.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4085.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4086.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4088.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4089.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4091.ConnectorPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4093.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4094.CouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4096.CVTPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4097.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4098.CycloidalAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(_4098.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4101.CycloidalDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(_4101.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4104.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4105.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(_4105.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4106.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4107.DatumPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4108.ExternalCADModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4110.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4111.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4114.FEPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4115.FlexiblePinAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4117.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.GearPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4118.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4119.GuideDxfModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4121.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4122.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4125.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(
                _4125.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(
                _4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(
                _4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(
                _4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(
                _4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4133.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4134.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4136.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.OilSealPowerFlow)

        @property
        def part_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4139.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4140.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4142.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4143.PlanetCarrierPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4144.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4147.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4148.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4149.RingPinsPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4151.RollingRingAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4153.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4154.RootAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4155.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4156.ShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4160.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4161.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4163.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4164.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4166.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4167.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4169.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4170.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4171.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4172.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4172

            return self._parent._cast(_4172.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4173.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4173

            return self._parent._cast(_4173.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4174.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4174

            return self._parent._cast(_4174.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4175.SynchroniserPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4175

            return self._parent._cast(_4175.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4176.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4176

            return self._parent._cast(_4176.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4179.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4179

            return self._parent._cast(_4179.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4180.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4180

            return self._parent._cast(_4180.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4181.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4181

            return self._parent._cast(_4181.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4182.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4182

            return self._parent._cast(_4182.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4183.VirtualComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4183

            return self._parent._cast(_4183.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4185.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4185

            return self._parent._cast(_4185.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4186.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4186

            return self._parent._cast(_4186.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4188.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4188

            return self._parent._cast(_4188.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4189.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4189

            return self._parent._cast(_4189.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4596.AbstractShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4597.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4600.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4601.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4602.AssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4603.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.BearingModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4605.BeltDriveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4607.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4608.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4609.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4610.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4612.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4613.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4614.BoltedJointModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4615.BoltModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4617.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4618.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ClutchModalAnalysis)

        @property
        def component_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4622.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4623.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4625.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4626.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4628.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4629.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.ConicalGearSetModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4631.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4634.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4635.CouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4637.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4638.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4639.CycloidalAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4641.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4644.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4645.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(_4645.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4646.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(_4646.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4647.DatumModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(_4647.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4651.ExternalCADModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(_4651.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4653.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(_4653.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4654.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4655.FEPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4656.FlexiblePinAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656

            return self._parent._cast(_4656.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4659.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4660.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4661.GuideDxfModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4663.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(_4663.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4664.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4667.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(
                _4667.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4668.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(
                _4668.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4670.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(
                _4670.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(
                _4671.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4673.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(
                _4673.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(
                _4674.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4675.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4676.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4681.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4683.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.OilSealModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4687.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4688.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4690.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4691.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4692.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4693.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4694.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4695.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.RingPinsModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4697.RollingRingAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4699.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4700.RootAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4701.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4702.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.ShaftModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4705.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4707.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4708.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4710.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4711.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4713.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4714.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4716.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4717.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4718.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4718

            return self._parent._cast(_4718.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4719.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4719

            return self._parent._cast(_4719.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4720.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4720

            return self._parent._cast(_4720.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4721.SynchroniserModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4721

            return self._parent._cast(_4721.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4722.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4722

            return self._parent._cast(_4722.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4723.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4723

            return self._parent._cast(_4723.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4725.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4725

            return self._parent._cast(_4725.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4726.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4726

            return self._parent._cast(_4726.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4727.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4727

            return self._parent._cast(_4727.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4728.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4728

            return self._parent._cast(_4728.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4729.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4729

            return self._parent._cast(_4729.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4734.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4734

            return self._parent._cast(_4734.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4735.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4735

            return self._parent._cast(_4735.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4737.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4737

            return self._parent._cast(_4737.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4738.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4738

            return self._parent._cast(_4738.ZerolBevelGearSetModalAnalysis)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4880.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(_4880.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4881.AbstractShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(_4881.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4882.AbstractShaftOrHousingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(
                _4882.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4885.AGMAGleasonConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4885,
            )

            return self._parent._cast(
                _4885.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(
                _4886.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4887.AssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4887,
            )

            return self._parent._cast(_4887.AssemblyModalAnalysisAtAStiffness)

        @property
        def bearing_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4888.BearingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.BearingModalAnalysisAtAStiffness)

        @property
        def belt_drive_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4890.BeltDriveModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.BeltDriveModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4892.BevelDifferentialGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(
                _4892.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4893.BevelDifferentialGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(
                _4893.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4894.BevelDifferentialPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(
                _4894.BevelDifferentialPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4895.BevelDifferentialSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4895,
            )

            return self._parent._cast(
                _4895.BevelDifferentialSunGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4897.BevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4897,
            )

            return self._parent._cast(_4897.BevelGearModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4898.BevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4898,
            )

            return self._parent._cast(_4898.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def bolted_joint_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4899.BoltedJointModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4899,
            )

            return self._parent._cast(_4899.BoltedJointModalAnalysisAtAStiffness)

        @property
        def bolt_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4900.BoltModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4900,
            )

            return self._parent._cast(_4900.BoltModalAnalysisAtAStiffness)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4902.ClutchHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4902,
            )

            return self._parent._cast(_4902.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def clutch_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4903.ClutchModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.ClutchModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4905.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.ComponentModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4907.ConceptCouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4907,
            )

            return self._parent._cast(
                _4907.ConceptCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4908.ConceptCouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4908,
            )

            return self._parent._cast(_4908.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def concept_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4910.ConceptGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4910,
            )

            return self._parent._cast(_4910.ConceptGearModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4911.ConceptGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4911,
            )

            return self._parent._cast(_4911.ConceptGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4913.ConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.ConicalGearModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4914.ConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4916.ConnectorModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4916,
            )

            return self._parent._cast(_4916.ConnectorModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4918.CouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4919.CouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4919,
            )

            return self._parent._cast(_4919.CouplingModalAnalysisAtAStiffness)

        @property
        def cvt_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4921.CVTModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4921,
            )

            return self._parent._cast(_4921.CVTModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4922.CVTPulleyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(_4922.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4923.CycloidalAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4923,
            )

            return self._parent._cast(_4923.CycloidalAssemblyModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4925.CycloidalDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(_4925.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4928.CylindricalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4928,
            )

            return self._parent._cast(_4928.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4929.CylindricalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4929,
            )

            return self._parent._cast(_4929.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4930.CylindricalPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(
                _4930.CylindricalPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def datum_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4931.DatumModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4931,
            )

            return self._parent._cast(_4931.DatumModalAnalysisAtAStiffness)

        @property
        def external_cad_model_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4933.ExternalCADModelModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.ExternalCADModelModalAnalysisAtAStiffness)

        @property
        def face_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4935.FaceGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.FaceGearModalAnalysisAtAStiffness)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4936.FaceGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(_4936.FaceGearSetModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4937.FEPartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.FEPartModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4938.FlexiblePinAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(
                _4938.FlexiblePinAssemblyModalAnalysisAtAStiffness
            )

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4940.GearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.GearModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4941.GearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4941,
            )

            return self._parent._cast(_4941.GearSetModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4942.GuideDxfModelModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4942,
            )

            return self._parent._cast(_4942.GuideDxfModelModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4944.HypoidGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.HypoidGearModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4945.HypoidGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4945,
            )

            return self._parent._cast(_4945.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4948.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4948,
            )

            return self._parent._cast(
                _4948.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4949.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4949,
            )

            return self._parent._cast(
                _4949.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4951.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4951,
            )

            return self._parent._cast(
                _4951.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4952.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4952,
            )

            return self._parent._cast(
                _4952.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4954.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4954,
            )

            return self._parent._cast(
                _4954.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> (
            "_4955.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4955,
            )

            return self._parent._cast(
                _4955.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4956.MassDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(_4956.MassDiscModalAnalysisAtAStiffness)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4957.MeasurementComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(
                _4957.MeasurementComponentModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4959.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.MountableComponentModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4960.OilSealModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4960,
            )

            return self._parent._cast(_4960.OilSealModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4963.PartToPartShearCouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4963,
            )

            return self._parent._cast(
                _4963.PartToPartShearCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4964.PartToPartShearCouplingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(
                _4964.PartToPartShearCouplingModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4966.PlanetaryGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(_4966.PlanetaryGearSetModalAnalysisAtAStiffness)

        @property
        def planet_carrier_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4967.PlanetCarrierModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4967,
            )

            return self._parent._cast(_4967.PlanetCarrierModalAnalysisAtAStiffness)

        @property
        def point_load_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4968.PointLoadModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4968,
            )

            return self._parent._cast(_4968.PointLoadModalAnalysisAtAStiffness)

        @property
        def power_load_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4969.PowerLoadModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4969,
            )

            return self._parent._cast(_4969.PowerLoadModalAnalysisAtAStiffness)

        @property
        def pulley_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4970.PulleyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4970,
            )

            return self._parent._cast(_4970.PulleyModalAnalysisAtAStiffness)

        @property
        def ring_pins_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4971.RingPinsModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4971,
            )

            return self._parent._cast(_4971.RingPinsModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4973.RollingRingAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4973,
            )

            return self._parent._cast(
                _4973.RollingRingAssemblyModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4975.RollingRingModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4975,
            )

            return self._parent._cast(_4975.RollingRingModalAnalysisAtAStiffness)

        @property
        def root_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4976.RootAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4976,
            )

            return self._parent._cast(_4976.RootAssemblyModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4977.ShaftHubConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4977,
            )

            return self._parent._cast(_4977.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4978.ShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(_4978.ShaftModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4980.SpecialisedAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(
                _4980.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4982.SpiralBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4983.SpiralBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4983,
            )

            return self._parent._cast(_4983.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4985.SpringDamperHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4985,
            )

            return self._parent._cast(_4985.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def spring_damper_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4986.SpringDamperModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4986,
            )

            return self._parent._cast(_4986.SpringDamperModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4988.StraightBevelDiffGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4988,
            )

            return self._parent._cast(
                _4988.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4989.StraightBevelDiffGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4989,
            )

            return self._parent._cast(
                _4989.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4991.StraightBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4991,
            )

            return self._parent._cast(_4991.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4992.StraightBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4992,
            )

            return self._parent._cast(
                _4992.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4993.StraightBevelPlanetGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4993,
            )

            return self._parent._cast(
                _4993.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4994.StraightBevelSunGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4994,
            )

            return self._parent._cast(
                _4994.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4995.SynchroniserHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4995,
            )

            return self._parent._cast(_4995.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4996.SynchroniserModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4996,
            )

            return self._parent._cast(_4996.SynchroniserModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4997.SynchroniserPartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4997,
            )

            return self._parent._cast(_4997.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_4998.SynchroniserSleeveModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4998,
            )

            return self._parent._cast(_4998.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5000.TorqueConverterModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5000,
            )

            return self._parent._cast(_5000.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5001.TorqueConverterPumpModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5001,
            )

            return self._parent._cast(
                _5001.TorqueConverterPumpModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5002.TorqueConverterTurbineModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5002,
            )

            return self._parent._cast(
                _5002.TorqueConverterTurbineModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5003.UnbalancedMassModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5003,
            )

            return self._parent._cast(_5003.UnbalancedMassModalAnalysisAtAStiffness)

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5004.VirtualComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5004,
            )

            return self._parent._cast(_5004.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def worm_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5006.WormGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5006,
            )

            return self._parent._cast(_5006.WormGearModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5007.WormGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5007,
            )

            return self._parent._cast(_5007.WormGearSetModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5009.ZerolBevelGearModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5009,
            )

            return self._parent._cast(_5009.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5010.ZerolBevelGearSetModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5010,
            )

            return self._parent._cast(_5010.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5140.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(_5140.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5141.AbstractShaftModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.AbstractShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5142.AbstractShaftOrHousingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5146.AGMAGleasonConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(
                _5146.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5147.AssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5147,
            )

            return self._parent._cast(_5147.AssemblyModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5148.BearingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.BearingModalAnalysisAtASpeed)

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5150.BeltDriveModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5152.BevelDifferentialGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5153.BevelDifferentialGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(
                _5153.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(
                _5154.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5155.BevelDifferentialSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(
                _5155.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5157.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.BevelGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5158.BevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5158,
            )

            return self._parent._cast(_5158.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5159.BoltedJointModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5159,
            )

            return self._parent._cast(_5159.BoltedJointModalAnalysisAtASpeed)

        @property
        def bolt_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5160.BoltModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.BoltModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5162.ClutchHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5162,
            )

            return self._parent._cast(_5162.ClutchHalfModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5163.ClutchModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.ClutchModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5165.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.ComponentModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5167.ConceptCouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5167,
            )

            return self._parent._cast(_5167.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5168.ConceptCouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5168,
            )

            return self._parent._cast(_5168.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5170.ConceptGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5170,
            )

            return self._parent._cast(_5170.ConceptGearModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5171.ConceptGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5173.ConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.ConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5174.ConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5176.ConnectorModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5176,
            )

            return self._parent._cast(_5176.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5178.CouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(_5178.CouplingHalfModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5179.CouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(_5179.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5181.CVTModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(_5181.CVTModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5182.CVTPulleyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(_5182.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5183.CycloidalAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(_5183.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5185.CycloidalDiscModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(_5185.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5188.CylindricalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(_5188.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5189.CylindricalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5189,
            )

            return self._parent._cast(_5189.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5190.CylindricalPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(_5190.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def datum_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5191.DatumModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(_5191.DatumModalAnalysisAtASpeed)

        @property
        def external_cad_model_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5192.ExternalCADModelModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5192,
            )

            return self._parent._cast(_5192.ExternalCADModelModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5194.FaceGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.FaceGearModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5195.FaceGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(_5195.FaceGearSetModalAnalysisAtASpeed)

        @property
        def fe_part_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5196.FEPartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.FEPartModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5197.FlexiblePinAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5199.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.GearModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5200.GearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(_5200.GearSetModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5201.GuideDxfModelModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5201,
            )

            return self._parent._cast(_5201.GuideDxfModelModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5203.HypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.HypoidGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5204.HypoidGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5204,
            )

            return self._parent._cast(_5204.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5207.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5207,
            )

            return self._parent._cast(
                _5207.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5208.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(
                _5208.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5210.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(
                _5210.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5211.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5211,
            )

            return self._parent._cast(
                _5211.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5213.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(
                _5213.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5214.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(
                _5214.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
            )

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5215.MassDiscModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5215,
            )

            return self._parent._cast(_5215.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5216.MeasurementComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5218.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.MountableComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5219.OilSealModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(_5219.OilSealModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5220.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.PartModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5222.PartToPartShearCouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(
                _5222.PartToPartShearCouplingHalfModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5223.PartToPartShearCouplingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5223,
            )

            return self._parent._cast(
                _5223.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5225.PlanetaryGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(_5225.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def planet_carrier_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5226.PlanetCarrierModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(_5226.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5227.PointLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(_5227.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5228.PowerLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5229.PulleyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5229,
            )

            return self._parent._cast(_5229.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5230.RingPinsModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.RingPinsModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5232.RollingRingAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5232,
            )

            return self._parent._cast(_5232.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5234.RollingRingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.RollingRingModalAnalysisAtASpeed)

        @property
        def root_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5235.RootAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5235,
            )

            return self._parent._cast(_5235.RootAssemblyModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5236.ShaftHubConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5236,
            )

            return self._parent._cast(_5236.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5237.ShaftModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(_5237.ShaftModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5239.SpecialisedAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5241.SpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5242.SpiralBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5242,
            )

            return self._parent._cast(_5242.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5244.SpringDamperHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5244,
            )

            return self._parent._cast(_5244.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5245.SpringDamperModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5245,
            )

            return self._parent._cast(_5245.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5247.StraightBevelDiffGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5247,
            )

            return self._parent._cast(_5247.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5248.StraightBevelDiffGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5248,
            )

            return self._parent._cast(
                _5248.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5250.StraightBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5250,
            )

            return self._parent._cast(_5250.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5251.StraightBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5251,
            )

            return self._parent._cast(_5251.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5252.StraightBevelPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5252,
            )

            return self._parent._cast(
                _5252.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5253.StraightBevelSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5253,
            )

            return self._parent._cast(_5253.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5254.SynchroniserHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5254,
            )

            return self._parent._cast(_5254.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5255.SynchroniserModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5255,
            )

            return self._parent._cast(_5255.SynchroniserModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5256.SynchroniserPartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5256,
            )

            return self._parent._cast(_5256.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5257.SynchroniserSleeveModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5257,
            )

            return self._parent._cast(_5257.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5259.TorqueConverterModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5259,
            )

            return self._parent._cast(_5259.TorqueConverterModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5260.TorqueConverterPumpModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5260,
            )

            return self._parent._cast(_5260.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5261.TorqueConverterTurbineModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5261,
            )

            return self._parent._cast(_5261.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5262.UnbalancedMassModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5262,
            )

            return self._parent._cast(_5262.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5263.VirtualComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5263,
            )

            return self._parent._cast(_5263.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5265.WormGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5265,
            )

            return self._parent._cast(_5265.WormGearModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5266.WormGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5266,
            )

            return self._parent._cast(_5266.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5268.ZerolBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5268,
            )

            return self._parent._cast(_5268.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5269.ZerolBevelGearSetModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5269,
            )

            return self._parent._cast(_5269.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5704.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AbstractAssemblyHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5706.AbstractShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5707.AbstractShaftOrHousingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5709.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5711.AGMAGleasonConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5712.AssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.AssemblyHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5713.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.BearingHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5715.BeltDriveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5716.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5718.BevelDifferentialGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5719.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5720.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5721.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.BevelGearHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5723.BevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5724.BoltedJointHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(_5724.BoltedJointHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5725.BoltHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5725,
            )

            return self._parent._cast(_5725.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5727.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.ClutchHalfHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5728.ClutchHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.ClutchHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5733.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(_5733.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5734.ConceptCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5734,
            )

            return self._parent._cast(_5734.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5735.ConceptGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5735,
            )

            return self._parent._cast(_5735.ConceptGearHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5737.ConceptGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5737,
            )

            return self._parent._cast(_5737.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5738.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5738,
            )

            return self._parent._cast(_5738.ConicalGearHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5740.ConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(_5740.ConicalGearSetHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5742.ConnectorHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5742,
            )

            return self._parent._cast(_5742.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5744.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5744,
            )

            return self._parent._cast(_5744.CouplingHalfHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5745.CouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(_5745.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5747.CVTHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5747,
            )

            return self._parent._cast(_5747.CVTHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5748.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5749.CycloidalAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5751.CycloidalDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5753.CylindricalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5755.CylindricalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.CylindricalGearSetHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5756.CylindricalPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5756,
            )

            return self._parent._cast(_5756.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5757.DatumHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5757,
            )

            return self._parent._cast(_5757.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5772.ExternalCADModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5772,
            )

            return self._parent._cast(_5772.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5773.FaceGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(_5773.FaceGearHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5775.FaceGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5775,
            )

            return self._parent._cast(_5775.FaceGearSetHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5776.FEPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(_5776.FEPartHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5777.FlexiblePinAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(_5777.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5779.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(_5779.GearHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5784.GearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.GearSetHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5786.GuideDxfModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5797.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5797,
            )

            return self._parent._cast(_5797.HypoidGearHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5799.HypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(_5799.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5801.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(
                _5801.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5803.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(
                _5803.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5804.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(
                _5804.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5806.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(
                _5806.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5807.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(
                _5807.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5809.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(
                _5809.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5810.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5811.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5811,
            )

            return self._parent._cast(_5811.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5813.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.OilSealHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5816.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5817.PartToPartShearCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5820.PlanetaryGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.PlanetaryGearSetHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5821.PlanetCarrierHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5822.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5823.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5824.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5826.RingPinsHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5828.RollingRingAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.RollingRingAssemblyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5830.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.RollingRingHarmonicAnalysis)

        @property
        def root_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5831.RootAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5831,
            )

            return self._parent._cast(_5831.RootAssemblyHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5832.ShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5833.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.ShaftHubConnectionHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5836.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5838.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.SpiralBevelGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5840.SpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5842.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.SpringDamperHalfHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5843.SpringDamperHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5845.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5845,
            )

            return self._parent._cast(_5845.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5847.StraightBevelDiffGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5847,
            )

            return self._parent._cast(_5847.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5848.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5848,
            )

            return self._parent._cast(_5848.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5850.StraightBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5850,
            )

            return self._parent._cast(_5850.StraightBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5851.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5851,
            )

            return self._parent._cast(_5851.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5852.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5852,
            )

            return self._parent._cast(_5852.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5853.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5853,
            )

            return self._parent._cast(_5853.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5854.SynchroniserHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5854,
            )

            return self._parent._cast(_5854.SynchroniserHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5855.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5855,
            )

            return self._parent._cast(_5855.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5856.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5856,
            )

            return self._parent._cast(_5856.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5858.TorqueConverterHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5858,
            )

            return self._parent._cast(_5858.TorqueConverterHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5859.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5859,
            )

            return self._parent._cast(_5859.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5860.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5860,
            )

            return self._parent._cast(_5860.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5862.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5862,
            )

            return self._parent._cast(_5862.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5863.VirtualComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5863,
            )

            return self._parent._cast(_5863.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5864.WormGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5864,
            )

            return self._parent._cast(_5864.WormGearHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5866.WormGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5866,
            )

            return self._parent._cast(_5866.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5867.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5867,
            )

            return self._parent._cast(_5867.ZerolBevelGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_5869.ZerolBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5869,
            )

            return self._parent._cast(_5869.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6035.AbstractShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(
                _6035.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6036.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6038.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6040.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6041.AssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(_6041.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6042.BearingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(_6042.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6044.BeltDriveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(_6044.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6045.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6047.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(
                _6047.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6048.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6049.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(
                _6049.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6050.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(_6050.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6052.BevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6052,
            )

            return self._parent._cast(
                _6052.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6053.BoltedJointHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6053,
            )

            return self._parent._cast(
                _6053.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6054.BoltHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(_6054.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6056.ClutchHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(
                _6056.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6057.ClutchHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(_6057.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6061.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(
                _6061.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6062.ConceptCouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(
                _6062.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6063.ConceptGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(
                _6063.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6065.ConceptGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(
                _6065.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6066.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(
                _6066.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6068.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(
                _6068.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6070.ConnectorHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(_6070.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6072.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6072,
            )

            return self._parent._cast(
                _6072.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6073.CouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(_6073.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6075.CVTHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(_6075.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6076.CVTPulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(_6076.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6077.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6079.CycloidalDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6081.CylindricalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6083.CylindricalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6084.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6085.DatumHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6086.ExternalCADModelHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(
                _6086.ExternalCADModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6087.FaceGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(_6087.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6089.FaceGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6090.FEPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(_6090.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6091.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(
                _6091.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6092.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(_6092.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6094.GearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(_6094.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6095.GuideDxfModelHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.GuideDxfModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6097.HypoidGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(
                _6097.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6099.HypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(
                _6099.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6101.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(
                _6101.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6103.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> (
            "_6104.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6106.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6107.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(
                _6107.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6109.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6110.MassDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6111.MeasurementComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6113.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6114.OilSealHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(_6114.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6117.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6118.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6120.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6121.PlanetCarrierHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6122.PointLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(_6122.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6123.PowerLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(_6123.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6124.PulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(_6124.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6125.RingPinsHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(_6125.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6127.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6129.RollingRingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6130.RootAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(
                _6130.RootAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6131.ShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(_6131.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6132.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6135.SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6137.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6137,
            )

            return self._parent._cast(
                _6137.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6139.SpringDamperHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6139,
            )

            return self._parent._cast(
                _6139.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6140.SpringDamperHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6140,
            )

            return self._parent._cast(
                _6140.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6141.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6141,
            )

            return self._parent._cast(
                _6141.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6143.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6143,
            )

            return self._parent._cast(
                _6143.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6144.StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6144,
            )

            return self._parent._cast(
                _6144.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6146.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6146,
            )

            return self._parent._cast(
                _6146.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6147.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6147,
            )

            return self._parent._cast(
                _6147.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6148.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6148,
            )

            return self._parent._cast(
                _6148.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6149.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6149,
            )

            return self._parent._cast(
                _6149.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6150.SynchroniserHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6150,
            )

            return self._parent._cast(
                _6150.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6151.SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6151,
            )

            return self._parent._cast(
                _6151.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6152.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6152,
            )

            return self._parent._cast(
                _6152.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6154.TorqueConverterHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6154,
            )

            return self._parent._cast(
                _6154.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6155.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6155,
            )

            return self._parent._cast(
                _6155.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6156.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6156,
            )

            return self._parent._cast(
                _6156.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6157.UnbalancedMassHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6157,
            )

            return self._parent._cast(
                _6157.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6158.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6158,
            )

            return self._parent._cast(
                _6158.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6159.WormGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6159,
            )

            return self._parent._cast(_6159.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6161.WormGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6161,
            )

            return self._parent._cast(
                _6161.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6162.ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6162,
            )

            return self._parent._cast(
                _6162.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6164.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6164,
            )

            return self._parent._cast(
                _6164.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6303.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6304.AbstractShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6305.AbstractShaftOrHousingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6307.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6309.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6310.AssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6311.BearingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6313.BeltDriveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6314.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6316.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6317.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6318.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6319.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6321.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6322.BoltDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6323.BoltedJointDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6325.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6326.ClutchHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6328.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6330.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6331.ConceptCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6332.ConceptGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6334.ConceptGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6335.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6337.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6339.ConnectorDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6341.CouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(_6341.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6342.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6344.CVTDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(_6344.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6345.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6346.CycloidalAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(_6346.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6348.CycloidalDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(_6348.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6350.CylindricalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(_6350.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6352.CylindricalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6353.CylindricalPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6354.DatumDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6357.ExternalCADModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6358.FaceGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6360.FaceGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6361.FEPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6362.FlexiblePinAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6363.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6365.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6366.GuideDxfModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6367.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6369.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6371.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(
                _6371.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(
                _6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(
                _6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(
                _6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6377.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(
                _6377.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6379.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(
                _6379.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6380.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6381.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6382.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6383.OilSealDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6386.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6387.PartToPartShearCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6389.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6390.PlanetCarrierDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6391.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6392.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6393.PulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6394.RingPinsDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6396.RollingRingAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6398.RollingRingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6399.RootAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6400.ShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6401.ShaftHubConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6403.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6404.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6406.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6408.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6409.SpringDamperHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6409

            return self._parent._cast(_6409.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6410.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6410

            return self._parent._cast(_6410.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6412.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6413.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6413

            return self._parent._cast(_6413.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6415.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6416.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6416

            return self._parent._cast(_6416.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6417.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6417

            return self._parent._cast(_6417.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6418.SynchroniserDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6418

            return self._parent._cast(_6418.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6419.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6419

            return self._parent._cast(_6419.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6420.SynchroniserPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6420

            return self._parent._cast(_6420.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6421.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6421

            return self._parent._cast(_6421.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6423.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6423

            return self._parent._cast(_6423.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6424.TorqueConverterPumpDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6424

            return self._parent._cast(_6424.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6425.TorqueConverterTurbineDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6425

            return self._parent._cast(_6425.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6426.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6426

            return self._parent._cast(_6426.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6427.VirtualComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6427

            return self._parent._cast(_6427.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6428.WormGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6428

            return self._parent._cast(_6428.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6430.WormGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6430

            return self._parent._cast(_6430.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6431.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6431

            return self._parent._cast(_6431.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6433.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6433

            return self._parent._cast(_6433.ZerolBevelGearSetDynamicAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6569.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6570.AbstractShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6571.AbstractShaftOrHousingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(_6571.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6575.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(
                _6575.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6576.AssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.AssemblyCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6577.BearingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.BearingCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6579.BeltDriveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6579,
            )

            return self._parent._cast(_6579.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6580.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6582.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(
                _6582.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6583.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(
                _6583.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6584.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(
                _6584.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6585.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.BevelGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6587.BevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(_6587.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolt_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6588.BoltCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(_6588.BoltCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6589.BoltedJointCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6591.ClutchCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.ClutchCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6592.ClutchHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(_6592.ClutchHalfCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6596.ConceptCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6596,
            )

            return self._parent._cast(_6596.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6597.ConceptCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6597,
            )

            return self._parent._cast(_6597.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6598.ConceptGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.ConceptGearCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6600.ConceptGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6601.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.ConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6603.ConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6605.ConnectorCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6607.CouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(_6607.CouplingCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6608.CouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(_6608.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6613.CVTCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(_6613.CVTCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6614.CVTPulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(_6614.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6615.CycloidalAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6615,
            )

            return self._parent._cast(_6615.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6617.CycloidalDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(_6617.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6619.CylindricalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6621.CylindricalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6622.CylindricalPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def datum_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6623.DatumCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.DatumCriticalSpeedAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6624.ExternalCADModelCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.ExternalCADModelCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6625.FaceGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.FaceGearCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6627.FaceGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.FaceGearSetCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6628.FEPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(_6628.FEPartCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6629.FlexiblePinAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6630.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.GearCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6632.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6632,
            )

            return self._parent._cast(_6632.GearSetCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6633.GuideDxfModelCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6634.HypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(_6634.HypoidGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6636.HypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6636,
            )

            return self._parent._cast(_6636.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6638.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(
                _6638.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6640.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(
                _6640.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6641.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(
                _6641.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6643.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(
                _6643.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6644.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(
                _6644.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6646.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(
                _6646.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def mass_disc_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6647.MassDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6648.MeasurementComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6650.OilSealCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.OilSealCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6653.PartToPartShearCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(
                _6653.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6654.PartToPartShearCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(
                _6654.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6656.PlanetaryGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def planet_carrier_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6657.PlanetCarrierCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(_6657.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6658.PointLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6659.PowerLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(_6659.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6660.PulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(_6660.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6661.RingPinsCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(_6661.RingPinsCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6663.RollingRingAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6665.RollingRingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.RollingRingCriticalSpeedAnalysis)

        @property
        def root_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6666.RootAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.RootAssemblyCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6667.ShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6667,
            )

            return self._parent._cast(_6667.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6668.ShaftHubConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6670.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6671.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6671,
            )

            return self._parent._cast(_6671.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6673.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6673,
            )

            return self._parent._cast(_6673.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6675.SpringDamperCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6675,
            )

            return self._parent._cast(_6675.SpringDamperCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6676.SpringDamperHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6676,
            )

            return self._parent._cast(_6676.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6677.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6677,
            )

            return self._parent._cast(_6677.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6679.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6679,
            )

            return self._parent._cast(
                _6679.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6680.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6680,
            )

            return self._parent._cast(_6680.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6682.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6682,
            )

            return self._parent._cast(_6682.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6683.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6683,
            )

            return self._parent._cast(
                _6683.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6684.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6684,
            )

            return self._parent._cast(_6684.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6685.SynchroniserCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6685,
            )

            return self._parent._cast(_6685.SynchroniserCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6686.SynchroniserHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6686,
            )

            return self._parent._cast(_6686.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6687.SynchroniserPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6687,
            )

            return self._parent._cast(_6687.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6688.SynchroniserSleeveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6688,
            )

            return self._parent._cast(_6688.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6690.TorqueConverterCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6690,
            )

            return self._parent._cast(_6690.TorqueConverterCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6691.TorqueConverterPumpCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6691,
            )

            return self._parent._cast(_6691.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6692.TorqueConverterTurbineCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6692,
            )

            return self._parent._cast(_6692.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6693.UnbalancedMassCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6693,
            )

            return self._parent._cast(_6693.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6694.VirtualComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6694,
            )

            return self._parent._cast(_6694.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6695.WormGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6695,
            )

            return self._parent._cast(_6695.WormGearCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6697.WormGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6697,
            )

            return self._parent._cast(_6697.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6698.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6698,
            )

            return self._parent._cast(_6698.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_6700.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6700,
            )

            return self._parent._cast(_6700.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7032.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7033.AbstractShaftAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7034.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7034,
            )

            return self._parent._cast(
                _7034.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7042.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7043.AssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.AssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7045.BearingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7047.BeltDriveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7047,
            )

            return self._parent._cast(
                _7047.BeltDriveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7050.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7050,
            )

            return self._parent._cast(
                _7050.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> (
            "_7051.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7052.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7053.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7055.BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7055,
            )

            return self._parent._cast(
                _7055.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7056.BoltAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7056,
            )

            return self._parent._cast(
                _7056.BoltAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7057.BoltedJointAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.BoltedJointAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7058.ClutchAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.ClutchAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7060.ClutchHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7060,
            )

            return self._parent._cast(
                _7060.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7063.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7063,
            )

            return self._parent._cast(
                _7063.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7065.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7066.ConceptGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7066,
            )

            return self._parent._cast(
                _7066.ConceptGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7068.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7071.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7071,
            )

            return self._parent._cast(
                _7071.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7073.ConnectorAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7073,
            )

            return self._parent._cast(
                _7073.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7074.CouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7076.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7077.CVTAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7079.CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7080.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7080,
            )

            return self._parent._cast(
                _7080.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7081.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7081,
            )

            return self._parent._cast(
                _7081.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7084.CylindricalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7084,
            )

            return self._parent._cast(
                _7084.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7086.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7087.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7088.DatumAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.DatumAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7089.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7090.FaceGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.FaceGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7092.FaceGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7093.FEPartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.FEPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7094.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7094,
            )

            return self._parent._cast(
                _7094.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7095.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7097.GearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7098.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7098,
            )

            return self._parent._cast(
                _7098.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7100.HypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7102.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7104.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7106.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7107.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7109.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7110.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7112.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7113.MassDiscAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7114.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7114,
            )

            return self._parent._cast(
                _7114.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7116.OilSealAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7118.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> (
            "_7120.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7122.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7123.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7124.PointLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7124,
            )

            return self._parent._cast(
                _7124.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7125.PowerLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7126.PulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7126,
            )

            return self._parent._cast(
                _7126.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7127.RingPinsAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.RingPinsAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7129.RollingRingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7130.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7130,
            )

            return self._parent._cast(
                _7130.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7132.RootAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.RootAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7133.ShaftAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.ShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7134.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7137.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7137,
            )

            return self._parent._cast(
                _7137.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7139.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7139,
            )

            return self._parent._cast(
                _7139.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7140.SpringDamperAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7140,
            )

            return self._parent._cast(
                _7140.SpringDamperAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7142.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7142,
            )

            return self._parent._cast(
                _7142.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7143.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7143,
            )

            return self._parent._cast(
                _7143.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7145.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7145,
            )

            return self._parent._cast(
                _7145.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7146.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7146,
            )

            return self._parent._cast(
                _7146.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7148.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7148,
            )

            return self._parent._cast(
                _7148.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7149.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7149,
            )

            return self._parent._cast(
                _7149.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7150.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7150,
            )

            return self._parent._cast(
                _7150.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7151.SynchroniserAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7151,
            )

            return self._parent._cast(
                _7151.SynchroniserAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7152.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7152,
            )

            return self._parent._cast(
                _7152.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7153.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7153,
            )

            return self._parent._cast(
                _7153.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7154.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7154,
            )

            return self._parent._cast(
                _7154.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7155.TorqueConverterAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7155,
            )

            return self._parent._cast(
                _7155.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7157.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7157,
            )

            return self._parent._cast(
                _7157.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7158.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7158,
            )

            return self._parent._cast(
                _7158.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7159.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7159,
            )

            return self._parent._cast(
                _7159.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7160.VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7160,
            )

            return self._parent._cast(
                _7160.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7161.WormGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7161,
            )

            return self._parent._cast(
                _7161.WormGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7163.WormGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7163,
            )

            return self._parent._cast(
                _7163.WormGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7164.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7164,
            )

            return self._parent._cast(
                _7164.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7166.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7166,
            )

            return self._parent._cast(
                _7166.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7296.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7297.AbstractShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7298.AbstractShaftOrHousingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(
                _7298.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7303.AGMAGleasonConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(
                _7303.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(
                _7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7306.AssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.AssemblyAdvancedSystemDeflection)

        @property
        def bearing_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7307.BearingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.BearingAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7309.BeltDriveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7310.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(
                _7310.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7312.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(
                _7312.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7313.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(
                _7313.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7314.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(
                _7314.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7315.BevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.BevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7317.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7318.BoltAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7318,
            )

            return self._parent._cast(_7318.BoltAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7319.BoltedJointAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7320.ClutchAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7320,
            )

            return self._parent._cast(_7320.ClutchAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7322.ClutchHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(_7322.ClutchHalfAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7324.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ComponentAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7325.ConceptCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(_7325.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7327.ConceptCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7328.ConceptGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.ConceptGearAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7330.ConceptGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7331.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.ConicalGearAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7333.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.ConicalGearSetAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7335.ConnectorAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7337.CouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(_7337.CouplingAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7339.CouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7340.CVTAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(_7340.CVTAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7342.CVTPulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(_7342.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7343.CycloidalAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(_7343.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7344.CycloidalDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(_7344.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7347.CylindricalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(_7347.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7349.CylindricalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7351.CylindricalPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(
                _7351.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def datum_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7352.DatumAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7353.ExternalCADModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7354.FaceGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.FaceGearAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7356.FaceGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.FaceGearSetAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7357.FEPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.FEPartAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7358.FlexiblePinAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7358,
            )

            return self._parent._cast(_7358.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7359.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.GearAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7361.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.GearSetAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7362.GuideDxfModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7363.HypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.HypoidGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7365.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7365,
            )

            return self._parent._cast(_7365.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7367.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7367,
            )

            return self._parent._cast(
                _7367.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7369.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(
                _7369.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7370.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(
                _7370.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7372.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(
                _7372.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7373.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(
                _7373.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7375.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(
                _7375.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7377.MassDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(_7377.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7378.MeasurementComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(
                _7378.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def mountable_component_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7379.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7380.OilSealAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(_7380.OilSealAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7382.PartToPartShearCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7384.PartToPartShearCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(
                _7384.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7386.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def planet_carrier_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7387.PlanetCarrierAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(_7387.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7388.PointLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7389.PowerLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7390.PulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(_7390.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7391.RingPinsAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(_7391.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7393.RollingRingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(_7393.RollingRingAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7394.RollingRingAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(_7394.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def root_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7396.RootAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(_7396.RootAssemblyAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7397.ShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7398.ShaftHubConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7400.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7401.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7403.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(_7403.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7404.SpringDamperAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(_7404.SpringDamperAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7406.SpringDamperHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7406,
            )

            return self._parent._cast(_7406.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7407.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7407,
            )

            return self._parent._cast(
                _7407.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7409.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7409,
            )

            return self._parent._cast(
                _7409.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7410.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7410,
            )

            return self._parent._cast(_7410.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7412.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7412,
            )

            return self._parent._cast(
                _7412.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7413.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7413,
            )

            return self._parent._cast(
                _7413.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7414.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7414,
            )

            return self._parent._cast(
                _7414.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7415.SynchroniserAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7415,
            )

            return self._parent._cast(_7415.SynchroniserAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7416.SynchroniserHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7416,
            )

            return self._parent._cast(_7416.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7417.SynchroniserPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7417,
            )

            return self._parent._cast(_7417.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7418.SynchroniserSleeveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7418,
            )

            return self._parent._cast(_7418.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7419.TorqueConverterAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7419,
            )

            return self._parent._cast(_7419.TorqueConverterAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7421.TorqueConverterPumpAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7421,
            )

            return self._parent._cast(_7421.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7422.TorqueConverterTurbineAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7422,
            )

            return self._parent._cast(
                _7422.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7424.UnbalancedMassAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7424,
            )

            return self._parent._cast(_7424.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7425.VirtualComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7425,
            )

            return self._parent._cast(_7425.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7426.WormGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7426,
            )

            return self._parent._cast(_7426.WormGearAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7428.WormGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7428,
            )

            return self._parent._cast(_7428.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7429.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7429,
            )

            return self._parent._cast(_7429.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7431.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7431,
            )

            return self._parent._cast(_7431.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def part_fe_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "PartStaticLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartStaticLoadAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase":
        return self._Cast_PartStaticLoadAnalysisCase(self)
