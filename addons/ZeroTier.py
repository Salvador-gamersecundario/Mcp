import subprocess
import json
import re
import os
import sys
import time
import threading

casuario = """[0m[38;2;135;143;147m[48;2;148;158;163m▌[0m[38;2;155;167;173m[48;2;137;147;147m▋[0m[38;2;136;145;145m[48;2;141;148;148m▊[0m[38;2;145;151;151m[48;2;142;149;150m┎[0m[38;2;140;147;148m[48;2;148;158;160m▋[0m[38;2;199;207;207m[48;2;168;175;177m╵[0m[38;2;147;149;148m[48;2;152;155;153m▊[0m[38;2;177;179;178m[48;2;161;163;161m╻[0m[38;2;148;150;146m[48;2;163;167;165m▋[0m[38;2;215;217;214m[48;2;151;151;144m▍[0m[38;2;154;154;145m[48;2;149;149;139m╿[0m[38;2;146;146;141m[48;2;159;162;161m▋[0m[38;2;146;143;138m[48;2;149;149;146m▗[0m[38;2;147;146;138m[48;2;142;137;123m▋[0m[38;2;126;117;97m[48;2;163;156;138m▖[0m[38;2;142;130;104m[48;2;151;140;122m▃[0m[38;2;133;116;88m[48;2;144;130;108m▃[0m[38;2;127;107;76m[48;2;141;124;98m▄[0m[38;2;108;88;62m[48;2;151;131;102m┃[0m[38;2;121;104;77m[48;2;108;91;64m▘[0m[38;2;86;70;44m[48;2;104;89;62m▅[0m[38;2;58;44;22m[48;2;79;64;40m▄[0m[38;2;78;65;43m[48;2;50;37;18m▍[0m[38;2;21;13;10m[48;2;42;30;17m▗[0m[38;2;27;16;11m[48;2;128;101;83m▅[0m
[0m[38;2;130;140;140m[48;2;140;150;153m▋[0m[38;2;157;166;172m[48;2;149;160;166m◀[0m[38;2;138;143;148m[48;2;137;144;144m▖[0m[38;2;145;151;151m[48;2;142;148;148m◀[0m[38;2;138;144;144m[48;2;142;147;148m┗[0m[38;2;154;162;164m[48;2;181;185;188m▊[0m[38;2;153;153;155m[48;2;148;149;151m▅[0m[38;2;151;153;152m[48;2;167;167;167m▍[0m[38;2;61;59;59m[48;2;143;143;139m▂[0m[38;2;56;53;52m[48;2;174;174;168m▅[0m[38;2;57;48;50m[48;2;126;116;111m━[0m[38;2;188;162;151m[48;2;86;76;77m▖[0m[38;2;75;71;71m[48;2;52;44;45m⎺[0m[38;2;42;35;37m[48;2;54;47;48m┮[0m[38;2;98;88;79m[48;2;43;35;37m⎺[0m[38;2;41;34;35m[48;2;119;106;85m▆[0m[38;2;35;27;27m[48;2;116;99;73m▅[0m[38;2;48;34;27m[48;2;106;85;55m▃[0m[38;2;89;66;40m[48;2;110;88;60m┠[0m[38;2;173;154;124m[48;2;76;59;33m▎[0m[38;2;48;32;18m[48;2;64;48;25m▄[0m[38;2;62;49;34m[48;2;40;29;18m▶[0m[38;2;39;29;17m[48;2;20;11;6m▘[0m[38;2;48;38;32m[48;2;19;11;6m╶[0m[38;2;25;14;11m[48;2;53;37;31m▋[0m
[0m[38;2;124;133;135m[48;2;130;140;140m▅[0m[38;2;137;147;149m[48;2;150;160;163m▍[0m[38;2;151;156;161m[48;2;132;137;140m▎[0m[38;2;131;137;137m[48;2;139;145;145m▄[0m[38;2;136;140;139m[48;2;139;145;145m▄[0m[38;2;138;140;139m[48;2;153;156;158m▖[0m[38;2;63;60;63m[48;2;145;144;147m▗[0m[38;2;104;101;102m[48;2;35;33;34m▘[0m[38;2;23;22;22m[48;2;35;33;33m╸[0m[38;2;44;40;42m[48;2;61;57;61m▉[0m[38;2;103;94;97m[48;2;179;157;156m▋[0m[38;2;178;155;149m[48;2;60;45;39m▘[0m[38;2;72;62;52m[48;2;53;41;33m╻[0m[38;2;31;26;30m[48;2;51;44;46m▝[0m[38;2;37;32;34m[48;2;50;45;47m┻[0m[38;2;41;37;39m[48;2;33;29;31m▌[0m[38;2;35;30;34m[48;2;25;20;23m┅[0m[38;2;28;23;27m[48;2;21;16;19m▂[0m[38;2;47;34;19m[48;2;22;16;16m▝[0m[38;2;37;27;18m[48;2;80;63;42m▄[0m[38;2;123;105;88m[48;2;31;20;14m▃[0m[38;2;171;143;121m[48;2;29;22;13m▂[0m[38;2;113;92;75m[48;2;44;34;25m▖[0m[38;2;31;21;11m[48;2;53;40;33m▆[0m[38;2;72;57;49m[48;2;31;19;13m╼[0m
[0m[38;2;116;124;130m[48;2;120;130;135m▗[0m[38;2;120;125;128m[48;2;138;143;146m▌[0m[38;2;145;151;153m[48;2;124;128;130m▌[0m[38;2;120;122;120m[48;2;126;129;129m▅[0m[38;2;123;122;120m[48;2;131;132;129m▂[0m[38;2;65;64;63m[48;2;113;112;111m▗[0m[38;2;51;49;52m[48;2;24;22;24m▘[0m[38;2;28;26;29m[48;2;23;21;24m◆[0m[38;2;25;24;26m[48;2;38;36;38m⎼[0m[38;2;48;46;47m[48;2;101;93;93m▘[0m[38;2;131;112;107m[48;2;215;187;183m▎[0m[38;2;114;90;85m[48;2;69;52;41m▎[0m[38;2;83;71;64m[48;2;59;49;40m▂[0m[38;2;48;42;46m[48;2;56;51;54m┚[0m[38;2;42;38;42m[48;2;34;30;34m▖[0m[38;2;38;34;38m[48;2;31;27;30m╉[0m[38;2;34;29;33m[48;2;25;22;25m■[0m[38;2;25;20;24m[48;2;18;14;17m▘[0m[38;2;16;12;14m[48;2;10;7;9m╱[0m[38;2;9;7;7m[48;2;30;22;19m▅[0m[38;2;20;9;10m[48;2;113;93;81m▖[0m[38;2;156;129;109m[48;2;166;139;116m▅[0m[38;2;77;60;42m[48;2;158;131;108m▝[0m[38;2;127;103;88m[48;2;47;33;22m▄[0m[38;2;83;65;50m[48;2;37;22;6m▃[0m
[0m[38;2;115;124;128m[48;2;112;117;121m▌[0m[38;2;122;125;126m[48;2;109;111;113m▝[0m[38;2;134;136;136m[48;2;121;121;120m▊[0m[38;2;109;108;100m[48;2;113;113;109m▄[0m[38;2;105;97;84m[48;2;112;108;99m▂[0m[38;2;75;71;66m[48;2;28;25;25m▌[0m[38;2;14;12;14m[48;2;21;20;20m▅[0m[38;2;20;18;21m[48;2;34;32;37m▌[0m[38;2;99;109;138m[48;2;60;58;68m▅[0m[38;2;85;78;87m[48;2;114;106;114m╊[0m[38;2;214;176;169m[48;2;185;140;128m▼[0m[38;2;146;101;94m[48;2;57;44;37m▘[0m[38;2;47;38;36m[48;2;76;76;88m▋[0m[38;2;99;127;166m[48;2;57;58;69m╸[0m[38;2;44;42;50m[48;2;36;34;40m▎[0m[38;2;24;22;25m[48;2;29;27;30m▄[0m[38;2;15;13;17m[48;2;24;22;25m┸[0m[38;2;13;11;14m[48;2;19;17;20m▲[0m[38;2;7;6;8m[48;2;13;10;14m┑[0m[38;2;5;3;6m[48;2;8;6;9m┏[0m[38;2;17;9;9m[48;2;6;4;4m⎺[0m[38;2;16;7;6m[48;2;117;93;79m▖[0m[38;2;149;119;101m[48;2;161;131;108m▖[0m[38;2;150;121;101m[48;2;157;128;108m┹[0m[38;2;159;131;113m[48;2;151;123;109m▆[0m
[0m[38;2;113;114;110m[48;2;112;116;116m▄[0m[38;2;110;109;105m[48;2;102;99;93m▋[0m[38;2;114;110;100m[48;2;128;125;118m▖[0m[38;2;121;114;103m[48;2;104;94;79m▎[0m[38;2;67;56;50m[48;2;98;86;71m▗[0m[38;2;38;36;40m[48;2;10;7;9m╶[0m[38;2;56;74;102m[48;2;13;11;14m▗[0m[38;2;95;171;236m[48;2;60;63;72m▅[0m[38;2;124;110;134m[48;2;135;163;206m▗[0m[38;2;95;71;85m[48;2;144;129;132m▅[0m[38;2;70;21;32m[48;2;181;151;138m▃[0m[38;2;64;9;23m[48;2;43;29;28m▃[0m[38;2;39;28;32m[48;2;74;50;54m▲[0m[38;2;111;123;152m[48;2;67;72;99m▚[0m[38;2;75;167;232m[48;2;37;40;52m▆[0m[38;2;61;147;217m[48;2;35;41;55m▖[0m[38;2;25;23;29m[48;2;20;18;21m▃[0m[38;2;13;11;15m[48;2;16;14;18m┸[0m[38;2;12;10;13m[48;2;8;6;8m▎[0m[38;2;6;4;7m[48;2;2;1;3m▋[0m[38;2;4;2;3m[48;2;3;2;1m▍[0m[38;2;39;26;23m[48;2;4;1;1m▝[0m[38;2;90;70;59m[48;2;157;130;110m▖[0m[38;2;161;132;111m[48;2;158;129;108m▚[0m[38;2;164;137;117m[48;2;155;126;108m▗[0m
[0m[38;2;112;107;93m[48;2;111;112;101m▅[0m[38;2;110;104;88m[48;2;102;93;76m▊[0m[38;2;93;86;69m[48;2;111;104;87m▍[0m[38;2;121;112;97m[48;2;93;81;60m▌[0m[38;2;79;65;47m[48;2;16;9;8m▊[0m[38;2;11;8;13m[48;2;8;5;8m┮[0m[38;2;45;51;72m[48;2;10;8;11m▝[0m[38;2;40;47;75m[48;2;46;101;192m▖[0m[38;2;59;86;147m[48;2;135;144;201m▆[0m[38;2;110;82;94m[48;2;59;22;28m▋[0m[38;2;6;0;0m[48;2;49;0;7m▄[0m[38;2;6;1;1m[48;2;52;0;9m▅[0m[38;2;38;10;15m[48;2;49;26;34m●[0m[38;2;80;103;167m[48;2;53;53;81m▝[0m[38;2;45;62;115m[48;2;52;106;199m▄[0m[38;2;57;80;125m[48;2;32;29;38m▘[0m[38;2;31;24;31m[48;2;23;18;24m▃[0m[38;2;23;19;23m[48;2;17;13;16m▌[0m[38;2;7;3;6m[48;2;12;9;12m▗[0m[38;2;9;7;10m[48;2;5;3;4m▘[0m[38;2;7;4;4m[48;2;4;2;3m⎽[0m[38;2;7;5;5m[48;2;3;1;1m◼[0m[38;2;142;117;102m[48;2;35;24;19m▝[0m[38;2;133;107;91m[48;2;159;130;111m▖[0m[38;2;142;115;96m[48;2;160;131;112m▃[0m
[0m[38;2;102;91;67m[48;2;108;97;78m▃[0m[38;2;103;89;63m[48;2;108;95;71m▃[0m[38;2;80;67;47m[48;2;94;81;60m┃[0m[38;2;105;93;74m[48;2;86;72;47m▊[0m[38;2;72;60;39m[48;2;11;6;5m▋[0m[38;2;2;0;3m[48;2;4;2;5m▄[0m[38;2;2;2;2m[48;2;8;6;9m▅[0m[38;2;13;12;15m[48;2;30;33;46m▋[0m[38;2;38;36;43m[48;2;44;81;155m▅[0m[38;2;119;101;104m[48;2;39;37;52m▝[0m[38;2;201;182;177m[48;2;52;40;42m▄[0m[38;2;173;155;149m[48;2;61;48;44m╱[0m[38;2;18;14;17m[48;2;33;26;28m╵[0m[38;2;39;33;42m[48;2;18;38;84m▅[0m[38;2;42;52;91m[48;2;25;11;16m▘[0m[38;2;8;5;6m[48;2;3;2;3m▎[0m[38;2;10;8;10m[48;2;24;22;25m▄[0m[38;2;39;37;39m[48;2;26;23;26m╲[0m[38;2;12;7;10m[48;2;22;17;20m▝[0m[38;2;11;6;8m[48;2;8;3;4m╲[0m[38;2;8;4;5m[48;2;5;2;2m▄[0m[38;2;12;6;5m[48;2;6;2;2m▝[0m[38;2;20;12;7m[48;2;99;80;67m▉[0m[38;2;159;130;110m[48;2;149;122;103m▼[0m[38;2;166;139;117m[48;2;155;128;105m▗[0m
[0m[38;2;96;82;56m[48;2;101;89;65m▆[0m[38;2;101;87;59m[48;2;94;80;52m┛[0m[38;2;84;70;42m[48;2;67;54;29m▌[0m[38;2;78;63;37m[48;2;90;78;55m▄[0m[38;2;59;47;27m[48;2;14;8;7m▌[0m[38;2;0;0;2m[48;2;0;0;1m╵[0m[38;2;0;0;0m[48;2;2;2;3m▉[0m[38;2;11;10;12m[48;2;30;28;31m▌[0m[38;2;22;20;21m[48;2;37;35;37m▆[0m[38;2;31;15;23m[48;2;5;3;6m▝[0m[38;2;72;10;25m[48;2;202;182;178m▃[0m[38;2;31;24;28m[48;2;75;45;50m┺[0m[38;2;68;0;4m[48;2;31;22;33m▂[0m[38;2;39;17;33m[48;2;83;13;27m▘[0m[38;2;22;1;3m[48;2;56;4;12m▝[0m[38;2;32;0;7m[48;2;2;0;0m▖[0m[38;2;2;1;1m[48;2;8;6;6m▆[0m[38;2;26;22;23m[48;2;13;10;11m▝[0m[38;2;9;7;8m[48;2;24;19;22m▃[0m[38;2;15;10;11m[48;2;9;4;4m▍[0m[38;2;12;6;5m[48;2;9;3;2m╲[0m[38;2;11;5;1m[48;2;7;2;0m▅[0m[38;2;31;20;13m[48;2;140;117;103m▊[0m[38;2;150;121;103m[48;2;160;131;113m┱[0m[38;2;162;134;114m[48;2;153;122;99m╾[0m
[0m[38;2;85;69;40m[48;2;90;76;47m▅[0m[38;2;79;64;35m[48;2;88;73;43m▄[0m[38;2;76;61;32m[48;2;66;51;22m▌[0m[38;2;48;33;7m[48;2;65;49;22m▖[0m[38;2;74;60;33m[48;2;43;34;20m▎[0m[38;2;15;11;8m[48;2;1;1;1m▖[0m[38;2;0;0;0m[48;2;1;1;1m▋[0m[38;2;13;11;14m[48;2;6;5;6m▝[0m[38;2;18;17;20m[48;2;13;11;14m▘[0m[38;2;16;8;14m[48;2;4;2;4m▅[0m[38;2;22;5;12m[48;2;94;24;45m▎[0m[38;2;82;4;22m[48;2;74;1;16m╍[0m[38;2;89;1;15m[48;2;80;0;9m▆[0m[38;2;54;2;8m[48;2;90;4;16m▗[0m[38;2;29;6;6m[48;2;57;9;21m▊[0m[38;2;85;7;38m[48;2;47;0;14m▆[0m[38;2;42;2;18m[48;2;1;0;0m▖[0m[38;2;4;3;3m[48;2;8;7;8m▋[0m[38;2;2;0;1m[48;2;5;2;3m▮[0m[38;2;11;6;2m[48;2;7;2;1m▗[0m[38;2;6;1;0m[48;2;9;3;0m▮[0m[38;2;19;15;5m[48;2;12;5;2m▂[0m[38;2;74;59;48m[48;2;26;17;9m▝[0m[38;2;54;38;28m[48;2;129;102;83m▃[0m[38;2;119;94;77m[48;2;158;126;101m▂[0m
[0m[38;2;91;74;46m[48;2;74;57;29m▎[0m[38;2;73;56;27m[48;2;77;61;30m▋[0m[38;2;79;62;31m[48;2;66;49;19m▌[0m[38;2;10;12;3m[48;2;43;35;13m┏[0m[38;2;19;18;11m[48;2;44;34;15m▆[0m[38;2;74;74;57m[48;2;28;28;22m▂[0m[38;2;24;23;20m[48;2;7;5;7m▂[0m[38;2;3;2;4m[48;2;9;7;10m▘[0m[38;2;20;18;21m[48;2;14;12;15m▗[0m[38;2;15;8;14m[48;2;51;14;29m▉[0m[38;2;186;81;125m[48;2;42;14;26m▋[0m[38;2;20;5;8m[48;2;121;6;39m▊[0m[38;2;176;4;61m[48;2;112;0;24m▃[0m[38;2;77;5;21m[48;2;8;1;1m▌[0m[38;2;10;2;1m[48;2;18;6;4m▆[0m[38;2;28;3;6m[48;2;77;6;30m▖[0m[38;2;92;7;41m[48;2;40;5;18m▋[0m[38;2;4;3;3m[48;2;1;0;0m▝[0m[38;2;0;0;0m[48;2;2;1;1m▎[0m[38;2;5;2;1m[48;2;13;6;3m▍[0m[38;2;21;14;8m[48;2;13;6;2m▃[0m[38;2;25;18;9m[48;2;20;11;5m▌[0m[38;2;21;8;7m[48;2;24;13;11m╲[0m[38;2;23;14;9m[48;2;30;19;11m▋[0m[38;2;60;43;31m[48;2;194;162;136m▌[0m
[0m[38;2;63;46;21m[48;2;43;27;6m▋[0m[38;2;37;22;8m[48;2;70;52;24m▄[0m[38;2;25;13;5m[48;2;59;44;21m┲[0m[38;2;79;80;60m[48;2;24;22;13m▗[0m[38;2;127;133;93m[48;2;55;59;43m▅[0m[38;2;173;169;118m[48;2;141;134;95m┺[0m[38;2;170;165;110m[48;2;75;72;56m▖[0m[38;2;33;29;31m[48;2;15;13;16m▃[0m[38;2;14;12;15m[48;2;26;24;27m▚[0m[38;2;23;19;23m[48;2;85;54;65m▋[0m[38;2;201;78;130m[48;2;157;49;96m▊[0m[38;2;79;22;47m[48;2;18;7;12m▏[0m[38;2;12;4;6m[48;2;149;28;73m▅[0m[38;2;87;8;33m[48;2;3;0;1m▘[0m[38;2;4;0;1m[48;2;8;1;1m▋[0m[38;2;63;5;23m[48;2;17;2;3m▝[0m[38;2;87;10;36m[48;2;75;9;28m●[0m[38;2;46;16;20m[48;2;8;1;1m▖[0m[38;2;13;7;4m[48;2;4;2;0m▗[0m[38;2;22;14;6m[48;2;16;9;3m┏[0m[38;2;25;18;11m[48;2;15;8;2m▘[0m[38;2;38;27;20m[48;2;14;9;1m▂[0m[38;2;53;39;30m[48;2;20;9;5m▄[0m[38;2;60;46;35m[48;2;80;64;52m▋[0m[38;2;147;123;102m[48;2;91;75;60m▝[0m"""

RGB = [(255, 255, 255), (110, 74, 255), (106, 0, 255)]

def gradient_text(text, colors):
    length = len(text)
    num_colors = len(colors)
    result = ""
    for i, char in enumerate(text):
        color_index = (i * (num_colors - 1)) // length
        t = (i * (num_colors - 1)) / length - color_index
        color1 = colors[color_index]
        color2 = colors[color_index + 1] if color_index + 1 < num_colors else colors[color_index]
        r = int(color1[0] + (color2[0] - color1[0]) * t)
        g = int(color1[1] + (color2[1] - color1[1]) * t)
        b = int(color1[2] + (color2[2] - color1[2]) * t)
        result += f'\033[38;2;{r};{g};{b}m{char}'
    return result + '\033[0m'

def ocultar_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def mostrar_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def silencioso(comando):
    try:
        resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT)
        return resultado.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return None

def mostrar_progreso():
    for i in range(1, 11):
        sys.stdout.write(f"\033[2;0H{gradient_text('〘' + '◼ ' * i + '〙', RGB)}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\033[2;0H" + " " * 80 + "\r")
    sys.stdout.flush()

def instalar_chafa():
    ocultar_cursor()
    print(gradient_text("〚𖡼 〛Verificando instalación de Chafa...", RGB))
    chafa_instalado = subprocess.call(['which', 'chafa'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
    if not chafa_instalado:
        ocultar_cursor()
        print(gradient_text("〚⎘ 〛Chafa no está instalado. Instalando...", RGB))
        subprocess.run(['sudo', 'apt-get', 'update'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'chafa'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(gradient_text("〚✔ 〛Chafa ya está instalado.", RGB))

def instalar_zerotier():
    progreso_thread = threading.Thread(target=mostrar_progreso)
    progreso_thread.start()

    subprocess.run('curl -s https://install.zerotier.com | sudo bash', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run('sudo service zerotier-one start', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run('sudo chmod 755 /usr/sbin/zerotier-one && sudo pkill zerotier-one && echo "9993" | sudo tee /var/lib/zerotier-one/zerotier-one.port && sudo service zerotier-one restart', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run('sudo chown root:root /var/lib/zerotier-one/authtoken.secret && sudo chmod 600 /var/lib/zerotier-one/authtoken.secret', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    progreso_thread.join()
    sys.stdout.write("\033[2;0H" + " " * 80 + "\r") 
    sys.stdout.flush()
    print(gradient_text("〚✔ 〛ZeroTier instalado y configurado.", RGB))

def obtener_ip_zerotier():
    print(gradient_text("〚𖡼 〛Obteniendo IP de ZeroTier...", RGB))
    intentos = 10
    ip = None
    
    for _ in range(intentos):
        redes = silencioso('sudo zerotier-cli listnetworks')
        if redes:
            ip_Zero = re.search(r'(\d+\.\d+\.\d+\.\d+)', redes)
            if ip_Zero:
                ip = ip_Zero.group(1)
                break
        time.sleep(3)
    
    if ip:
        os.system('clear')
        print(gradient_text(f"〚✔ 〛IP de ZeroTier obtenida ", RGB))
    else:
        print(gradient_text("〚✖ 〛No se pudo obtener la IP de ZeroTier. Por favor, intentálo de nuevo.", RGB))
    
    return ip

def Menu():
    while True:
        os.system('clear')
        menu = [
            gradient_text("〚1〛Instalar ZeroTier", RGB),
            gradient_text("〚2〛Desactivar ZeroTier", RGB),
            gradient_text("〚3〛Salir", RGB),
        ]
        for line in menu:
            ocultar_cursor()
            print(line)
            mostrar_cursor()
        
        print(gradient_text("   \n〚➥ 〛Seleccioná una opción ❱ ", RGB), end='')
        opcion = input()

        if opcion == "1":
            os.system('clear')
            ocultar_cursor()
            print(gradient_text("〚⎙ 〛Iniciando instalación de ZeroTier...", RGB))

            instalar_chafa()

            os.system('clear')
            print(gradient_text("〚☰ 〛Si no sabés utilizar este servicio leé: https://www.youtube.com/watch?v=9I97YprLOys ", RGB))
            print(gradient_text("〚⠸ 〛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", RGB))
            print(gradient_text("〚⏎ 〛Si ya lo leíste apretá Enter para continuar...", RGB))
            print(gradient_text("    ", RGB))

            chafa_command = "chafa --size=20x10 --dither=diffusion --colors=truecolor sapo.jpg"
            ascii_image = os.popen(chafa_command).read()
            input(ascii_image)
            os.system('clear')
            print(gradient_text('〚🡻 〛Descargando e instalando ZeroTier...', RGB))

            sys.stdout.write("\033[2;0H")
            sys.stdout.flush()

            progreso_thread = threading.Thread(target=mostrar_progreso)
            progreso_thread.start()
            instalar_zerotier()
            progreso_thread.join()
            sys.stdout.write("\033[2;0H" + " " * 80 + "\r") 
            sys.stdout.flush()
            print(gradient_text("〚✔ 〛ZeroTier instalado!", RGB))
            time.sleep(2)
            os.system('clear')

            print(gradient_text("〚✔ 〛ZeroTier instalado!\n〚⠸ 〛━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n〚☰ 〛Network ID\n  \n〚➥ 〛Colocá la ID de tu Network ❱ ", RGB), end='')
            mostrar_cursor()
            while True:
                network_id = input().strip()
                if len(network_id) == 16:
                    break
                else:
                    os.system('clear')
                    print(gradient_text("〚✖ 〛Error: La ID de la red no puede exceder 16 caracteres. Inténtalo de nuevo.", RGB))
                    print(casuario)
                    time.sleep(2)
                    os.system('clear')
                    print(gradient_text("〚✔ 〛ZeroTier instalado!\n〚⠸ 〛━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n〚☰ 〛Network ID\n  \n〚➥ 〛Colocá la ID de tu Network ❱ ", RGB), end='')
            ocultar_cursor()
            join_command = f'sudo zerotier-cli join {network_id}'
            subprocess.run(join_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            os.system('clear')

            ocultar_cursor()
            print(gradient_text("〚⎙ 〛Configurando tu ID...", RGB))
            time.sleep(2)
            os.system('clear')
            ip = obtener_ip_zerotier()
            if ip:
                config_path = "configuracion.json"
                try:
                    if os.path.exists(config_path):
                        with open(config_path, 'r') as file:
                            config = json.load(file)
                    else:
                        config = {}

                    config["servicio_a_usar"] = " "                
                    addons_dir = 'addons'
                    os.makedirs(addons_dir, exist_ok=True) 
                    with open(os.path.join(addons_dir, 'Ip-de-servidor.json'), 'w') as file:
                        json.dump({"ip": ip}, file)
                    with open(os.path.join(addons_dir, 'ZeroTier.json'), 'w') as file:
                        json.dump({"Activo": True}, file)
                    with open(config_path, 'w') as file:
                        json.dump(config, file)
                    
                    print(gradient_text(f"〚✔ 〛Servidor configurado en: ZeroTier", RGB))
                    print(gradient_text(f"〚⠸ 〛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n〚❯❱〛 La IP de tu servidor es: {ip}", RGB))
                    print(gradient_text(f"                                             ", RGB))
                    input(gradient_text("〚⏎ 〛Apretá enter para continuar...", RGB))
                    mostrar_cursor()
                except (IOError, json.JSONDecodeError) as e:
                    print(gradient_text(f"〚✖ 〛Error al procesar el archivo de configuración: {e}", RGB))   
            break

        elif opcion == "2":
            os.system('clear')
            ocultar_cursor()
            print(gradient_text("〚⛒ 〛Desactivando ZeroTier...", RGB))
            sys.stdout.write("\033[2;0H")
            sys.stdout.flush()

            for i in range(1, 11):    
                sys.stdout.write(f"\033[2;0H{gradient_text('〘' + '◼ ' * i + '〙', RGB)}")
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\033[2;0H" + " " * 80 + "\r") 
            print(gradient_text("〚✔ 〛ZeroTier desactivado!", RGB))
            sys.stdout.write("\033[?25h")

            archivo_zero_tier = 'addons/ZeroTier.json'
            if os.path.exists(archivo_zero_tier):
                os.remove(archivo_zero_tier)
            break

        elif opcion == "3":
            ocultar_cursor()
            sys.stdout.write("\r" + " " * 80 + "\r")
            sys.stdout.flush()
            print(gradient_text("〚❮❰ 〛Saliendo al menu...", RGB))
            time.sleep(2)
            break

        else:
            ocultar_cursor()
            print(gradient_text("〚✖ 〛Opción inválida. Por favor, seleccioná una opción del 1 al 3. ", RGB))

def verificar_activo():
    archivo_zero_tier = 'addons/ZeroTier.json'
    if os.path.exists(archivo_zero_tier):
        with open(archivo_zero_tier, 'r') as file:
            datos = json.load(file)
        datos["Activo"] = True
        with open(archivo_zero_tier, 'w') as file:
            json.dump(datos, file)
        comandos = [
            'sudo service zerotier-one start',
            'sudo chown root:root /var/lib/zerotier-one/authtoken.secret',
            'sudo chmod 600 /var/lib/zerotier-one/authtoken.secret',
            'sudo zerotier-cli listnetworks'
        ]
        for comando in comandos:
            silencioso(comando)

verificar_activo()