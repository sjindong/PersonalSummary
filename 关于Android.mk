一.平台编译报错，但这些错误 无关紧要
Reading library jar [/media/bak_data/data/shengjindong/eM10/out/target/common/obj/JAVA_LIBRARIES/volley_intermediates/classes.jar]
Warning: okio.DeflaterSink: can't find referenced class org.codehaus.mojo.animal_sniffer.IgnoreJRERequirement
Warning: okio.Okio: can't find referenced class java.nio.file.Files
Warning: okio.Okio: can't find referenced class java.nio.file.Files
Warning: okio.Okio: can't find referenced class java.nio.file.Files
Warning: okio.Okio: can't find referenced class java.nio.file.Path
Warning: okio.Okio: can't find referenced class java.nio.file.OpenOption
Warning: okio.Okio: can't find referenced class java.nio.file.Path
Warning: okio.Okio: can't find referenced class java.nio.file.OpenOption
Warning: okio.Okio: can't find referenced class org.codehaus.mojo.animal_sniffer.IgnoreJRERequirement
Warning: okio.Okio: can't find referenced class java.nio.file.Path
Warning: okio.Okio: can't find referenced class java.nio.file.OpenOption
Warning: okio.Okio: can't find referenced class java.nio.file.Path
Warning: okio.Okio: can't find referenced class java.nio.file.OpenOption
Warning: okio.Okio: can't find referenced class org.codehaus.mojo.animal_sniffer.IgnoreJRERequirement
Warning: there were 14 unresolved references to classes or interfaces.
         You may need to add missing library jars or update their versions.
         If your code works fine without the missing classes, you can suppress
         the warnings with '-dontwarn' options.
         (http://proguard.sourceforge.net/manual/troubleshooting.html#unresolvedclass)
Error: Please correct the above warnings first.
解决方案：
1.android.mk添加命令 LOCAL_PROGUARD_FLAG_FILES := proguard.cfg
2.和android.mk同目录下，添加文件proguard.cfg，文件内容：-dontwarn okio.**
