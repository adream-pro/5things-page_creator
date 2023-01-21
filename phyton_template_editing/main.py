from question import get_info
from write_file import write_html
from rename import rename_file

page_info = get_info()


html = f'''

<!DOCTYPE html>
<html lang=en>
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-C2Y71CJ9D0"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","G-C2Y71CJ9D0");</script>
<meta charset=UTF-8>
<meta http-equiv=X-UA-Compatible content="IE=edge">
<meta name=viewport content="width=device-width, initial-scale=1.0">
<link rel=stylesheet href=articlestyle.css>
<title>{page_info['sujet']}</title>
</head>
<body>
<script type=module>
        // Import the functions you need from the SDKs you need
        import {{ initializeApp }}from "https://www.gstatic.com/firebasejs/9.15.0/firebase-app.js";
        import {{ getAnalytics }} from "https://www.gstatic.com/firebasejs/9.15.0/firebase-analytics.js";
        // TODO: Add SDKs for Firebase products that you want to use
        // https://firebase.google.com/docs/web/setup#available-libraries
      
        // Your web app's Firebase configuration
        // For Firebase JS SDK v7.20.0 and later, measurementId is optional
        const firebaseConfig = {{
          apiKey: "AIzaSyAK_rnwmMW3NhZvdI0KboH0xdHp1okzQIY",
          authDomain: "top5ofthings-75cca.firebaseapp.com",
          projectId: "top5ofthings-75cca",
          storageBucket: "top5ofthings-75cca.appspot.com",
          messagingSenderId: "533157883172",
          appId: "1:533157883172:web:c3266e29920b48528d17b1",
          measurementId: "G-G7QK13J3CJ"
        }};
      
        // Initialize Firebase
        const app = initializeApp(firebaseConfig);
        const analytics = getAnalytics(app);
      </script>
<header>
<nav class=navbar>
<a href=../index.html class=nav-branding>Top Of Things</a>
<ul class=nav-menu>
<li class=nav-item>
<a href=lifestyle.html class=nav-link>Lifestyle</a>
</li>
<li class=nav-item>
<a href=travel.html class=nav-link>Travels</a>
</li>
<li class=nav-item>
<a href=other.html class=nav-link>Other</a>
</li>
<li class=nav-item>
<a href=about.html class=nav-link>About</a>
</li>
</ul>
<div class=hamburger>
<span class=bar></span>
<span class=bar></span>
<span class=bar></span>
</div>
</nav>
</header>
<div class=container>
<main class=grid>
<article>
<div class=title><h1>{page_info['sujet']}</h1></div>
<img src=../images/image1.jpg alt>
<div class=text>
<h3>{page_info['titre1']}</h3>
<p>{page_info['texte1']}</p>
</div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3857201619276158" crossorigin=anonymous></script>
<ins class=adsbygoogle style=display:block data-ad-client=ca-pub-3857201619276158 data-ad-slot=6183555382 data-ad-format=auto data-full-width-responsive=true></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
<img src=../images/image1.jpg alt>
<div class=text>
<h3>{page_info['titre2']}</h3>
<p>{page_info['texte2']}</p>
</div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3857201619276158" crossorigin=anonymous></script>
<ins class=adsbygoogle style=display:block data-ad-client=ca-pub-3857201619276158 data-ad-slot=6183555382 data-ad-format=auto data-full-width-responsive=true></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
<img src=../images/image1.jpg alt>
<div class=text>
<h3>{page_info['titre3']}</h3>
<p>{page_info['texte3']}</p>
</div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3857201619276158" crossorigin=anonymous></script>
<ins class=adsbygoogle style=display:block data-ad-client=ca-pub-3857201619276158 data-ad-slot=6183555382 data-ad-format=auto data-full-width-responsive=true></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
<img src=../images/image1.jpg alt>
<div class=text>
<h3>{page_info['titre4']}</h3>
<p>{page_info['texte4']}</p>
</div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3857201619276158" crossorigin=anonymous></script>
<ins class=adsbygoogle style=display:block data-ad-client=ca-pub-3857201619276158 data-ad-slot=6183555382 data-ad-format=auto data-full-width-responsive=true></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
<img src=../images/image1.jpg alt>
<div class=text>
<h3>{page_info['titre5']}</h3>
<p>{page_info['texte5']}</p>
</div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3857201619276158" crossorigin=anonymous></script>
<ins class=adsbygoogle style=display:block data-ad-client=ca-pub-3857201619276158 data-ad-slot=6183555382 data-ad-format=auto data-full-width-responsive=true></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
</article>
</main>
</div>
<script src=articlescript.js></script>
</body>
</html>

'''

write_html(page_info)
rename_file(page_info,html)


#{page_info['sujet']}




