#!/usr/bin/env python3
"""Tree(Indochina Travel)向け マンガ7日間行程の提案ページ。 python3 build.py -> index.html"""
import json, html

# 写真は「ワクワク採点」で選ぶ。建物の外観でなく、そこで人が楽しんでいる絵を最優先。
# 採点と選定理由は photos.json の score / note を見る。
PH = json.load(open('photos.json'))
gm = lambda q: 'https://www.google.com/maps/search/?api=1&query=' + q.replace(' ', '+')
emb = lambda q: 'https://maps.google.com/maps?q=' + q.replace(' ', '+') + '&output=embed&z=12'
def route_emb(stops):
    s = [x.replace(' ', '+') for x in stops]
    return 'https://maps.google.com/maps?saddr=' + s[0] + '&daddr=' + '+to:'.join(s[1:]) + '&output=embed'
def route_link(stops):
    s = [x.replace(' ', '+') for x in stops]
    return ('https://www.google.com/maps/dir/?api=1&origin=' + s[0] + '&destination=' + s[-1]
            + ('&waypoints=' + '%7C'.join(s[1:-1]) if len(s) > 2 else '') + '&travelmode=transit')

DAYS = [
 dict(id='1', city='Tokyo', chips=['Full day','Akihabara','The small shops'], name='Akihabara, top to bottom', tag='The district, floor by floor',
  why='One day in the anime and manga district, done properly: the big buildings everyone knows and the small shops most visitors never find. No queues for tickets, just walking and browsing.',
  steps=[('10:00','Meet at Akihabara Station','Electric Town exit. A quick map of the district and what each street is for.'),
         ('10:15','Radio Kaikan','Ten floors of figures, trading cards and model kits. The best place to see what is popular this month.'),
         ('11:30','Mandarake Complex','Eight floors of used manga, animation cels, vintage toys. Prices are honest and the finds are real.'),
         ('12:30','Lunch','See the picks below.'),
         ('14:00','Retro games and the back streets','Super Potato and the second-floor shops, where the district still looks like 2005.'),
         ('15:30','Maid cafe','Thirty minutes, one drink. It is part of the culture, and it is fun.'),
         ('16:30','Kanda Myojin shrine','The shrine that blesses electronics, ten minutes uphill. Anime-themed ema plaques and a quiet end to the day.'),
         ('17:30','Done','Evening free. Akihabara is loud until 20:00 if anyone wants more.')],
  stops=['Akihabara Station','Radio Kaikan Akihabara','Mandarake Complex Akihabara','Kanda Myojin Shrine'],
  moves='Everything is on foot. About 3 km over the day, with plenty of sitting.',
  food=[('Kyushu Jangara Ramen Akihabara','Akihabara · tonkotsu ramen','Rich pork broth on the main street since 1984. Fast, loud, and exactly what the district eats.','Kyushu Jangara Ramen Akihabara'),
        ('Kanda Matsuya','Kanda · soba since 1884','Handmade buckwheat noodles in an old wooden shop, ten minutes from the station. Quiet and very Tokyo.','Kanda Matsuya Soba')],
  good='Fans of any depth. Shoppers. Anyone who wants to see the district with someone who knows it.',
  mind='Sundays the main street is closed to cars and busier. Many shops open at 11:00, so mornings start with the big buildings.',
  links=[('Radio Kaikan','https://www.akihabara-radiokaikan.co.jp/'),('Mandarake','https://www.mandarake.co.jp/'),('Kanda Myojin','https://www.kandamyoujin.or.jp/')]),
 dict(id='2', city='Tokyo', chips=['Manga history','Tokiwa-so','Ikebukuro'], name='Tokiwa-so and Ikebukuro', tag='Where manga was born',
  why='The morning is the apartment where Tezuka, Fujiko Fujio and the other masters lived and drew in the 1950s, rebuilt exactly. The afternoon is Ikebukuro, the district that today serves fans as well as Akihabara does.',
  steps=[('10:00','Tokiwa-so Manga Museum','Shiinamachi, 20 minutes from Ikebukuro. The rebuilt 1952 apartment: the four-and-a-half-mat rooms, the shared kitchen, the stairs. Free entry, reserved slot.'),
         ('11:30','Tokiwa-so street walk','The neighbourhood monuments, the manga road, and the Chinese restaurant from the stories, still open.'),
         ('12:30','Lunch','See the picks below.'),
         ('14:00','Animate Ikebukuro flagship','Nine floors, the biggest anime shop in the world. Merchandise, books, the events floor.'),
         ('15:30','Otome Road','The street of second-hand shops (K-Books, Lashinbang) where rare goods surface first.'),
         ('17:00','Pokemon Center Mega Tokyo','In Sunshine City, five minutes away. Good for families and for gifts.'),
         ('18:00','Done','Evening free in Ikebukuro.')],
  stops=['Tokiwa-so Manga Museum','Shiinamachi Station','Animate Ikebukuro Flagship Store','Sunshine City Ikebukuro'],
  moves='Train Ikebukuro → Shiinamachi 5 min, then a 15-minute walk to the museum. Back to Ikebukuro by train. Afternoon on foot.',
  food=[('Matsuba','Shiinamachi · Chinese and ramen','The restaurant the Tokiwa-so artists ordered from, and drew into their manga. The same family runs it.','Matsuba Chinese Restaurant Shiinamachi'),
        ('Mutekiya','Ikebukuro · tonkotsu ramen','The line outside is the review. Thick pork broth, big portions, twenty minutes from ordering to done.','Mutekiya Ikebukuro')],
  good='Guests who want the history, not only the shopping. Good pacing after a full Akihabara day.',
  mind='Tokiwa-so museum is closed on Mondays. Entry is free but reserved in advance.',
  links=[('Tokiwa-so Manga Museum','https://tokiwasomm.jp/'),('Animate','https://www.animate.co.jp/')]),
 dict(id='3', city='Tokyo', chips=['Ghibli Museum','Advance tickets','Collectors'], name='Ghibli Museum and Nakano Broadway', tag='Ghibli, then the collectors’ arcade',
  why='The Ghibli Museum is the one place on the trip that needs planning months ahead, and it is worth it. The afternoon is Nakano Broadway, the arcade where Mandarake started, for original cels and rare comics.',
  steps=[('10:00','Ghibli Museum','Mitaka. Timed entry, tickets bought on the 10th of the previous month. The short film in the Saturn Theater, the Catbus room, the robot on the roof.'),
         ('12:30','Straw Hat Cafe and Inokashira Park','Lunch at the museum cafe, then a walk through the park to Kichijoji station.'),
         ('14:00','Nakano Broadway','Four floors and thirty specialist shops: animation cels, vintage manga, watches, toys. Mandarake’s original home.'),
         ('16:30','Daily Chiko','The eight-flavour soft serve in the basement. A Nakano rite of passage.'),
         ('17:00','Done','Nakano is five minutes from Shinjuku for the evening.')],
  stops=['Ghibli Museum Mitaka','Kichijoji Station','Nakano Broadway'],
  moves='Train to Mitaka 30 min from Shinjuku, then a 15-minute walk or the museum bus. Kichijoji → Nakano 10 min by train.',
  food=[('Straw Hat Cafe','Ghibli Museum · cafe','Inside the museum. Simple, good food: the omelette, the cutlet sandwich, the museum beer. Terrace tables outside.','Ghibli Museum Mitaka'),
        ('Daily Chiko','Nakano Broadway · soft serve','The tallest soft-serve cone in Tokyo, eight flavours stacked. Tiny stand in the basement food hall.','Daily Chiko Nakano Broadway')],
  good='Ghibli fans, families, anyone who loves the films. Collectors get their best afternoon here.',
  mind='Ghibli Museum is closed Tuesdays. Tickets sell out in minutes, so the trip dates are set around this day. No photos inside the museum.',
  links=[('Ghibli Museum','https://www.ghibli-museum.jp/en/'),('Nakano Broadway','https://www.nakano-broadway.com/')]),
 dict(id='4', city='Tokyo → Kyoto', chips=['Doraemon','Bullet train','Luggage forwarded'], name='Doraemon, then the bullet train', tag='Fujiko F. Fujio Museum to Kyoto',
  why='A morning with Doraemon at the museum built for him in Kawasaki, then the Shinkansen to Kyoto with the luggage already on its way hotel-to-hotel. Evening in the old shopping arcades and Gion.',
  steps=[('9:00','Luggage forwarded','Suitcases handed to the hotel desk. They arrive at the Kyoto hotel the next day, so the day is carried with a small bag only.'),
         ('10:00','Fujiko F. Fujio Museum','Noborito, 30 min from Shinjuku. Timed entry. Original drawings, the rooftop with Doraemon and the Anywhere Door, the museum cafe.'),
         ('12:00','Museum cafe lunch','See the picks below.'),
         ('13:30','Train to Shinagawa','40 minutes.'),
         ('14:30','Shinkansen Nozomi to Kyoto','2 hours 15. Mount Fuji on the right side about 45 minutes in, if the sky is clear.'),
         ('17:00','Check in','Kyoto hotel.'),
         ('18:00','Nishiki Market and Gion','The 400-year-old food arcade, then the Hanamikoji lanes at dusk. Done by 20:00.')],
  stops=['Fujiko F Fujio Museum Kawasaki','Shinagawa Station','Kyoto Station','Nishiki Market Kyoto','Hanamikoji Street Gion'],
  moves='Shinjuku → Noborito 30 min. Noborito → Shinagawa 40 min. Shinkansen 2h15. Kyoto Station → hotel by taxi.',
  food=[('Museum Cafe at Fujiko F. Fujio Museum','Kawasaki · museum cafe','Dishes shaped like the characters, Anki-pan French toast, Dorayaki. Kids and adults both order dessert.','Fujiko F Fujio Museum Kawasaki'),
        ('Nishiki Market','Kyoto · street food','Kyoto’s kitchen: grilled skewers, tamagoyaki, pickles, matcha sweets. Everyone picks their own along 400 metres.','Nishiki Market Kyoto')],
  good='Families. Anyone who wants the train ride to be part of the trip, not a transfer.',
  mind='The Doraemon museum is closed Tuesdays and needs timed tickets. Shinkansen seats are reserved in advance for the group.',
  links=[('Fujiko F. Fujio Museum','https://fujiko-museum.com/english.html'),('Luggage forwarding (Yamato)','https://www.kuronekoyamato.co.jp/en/')]),
 dict(id='5', city='Kyoto', chips=['50,000 volumes','Uji','Kyoto Animation'], name='Kyoto Manga Museum and Uji', tag='50,000 volumes, then matcha',
  why='A former elementary school holding 50,000 manga volumes, read anywhere including the lawn. Then Uji, thirty minutes south: the home town of Kyoto Animation, the Byodo-in temple, and the best matcha in Japan.',
  steps=[('10:00','Kyoto International Manga Museum','The Wall of Manga, 200 metres of shelves in a 1929 school building. Pick a series, sit on the lawn, read. Portrait artists on weekends.'),
         ('12:00','Lunch','See the picks below.'),
         ('13:30','Train to Uji','30 minutes on the JR Nara line.'),
         ('14:15','Byodo-in','The Phoenix Hall on the 10-yen coin, 1053. The museum next door holds the original phoenix statues.'),
         ('15:30','Uji tea street and Nakamura Tokichi','Matcha parfait, matcha soba, the tea shops along the river.'),
         ('16:30','Kyoto Animation locations','The Uji river bridges and the streets from Sound! Euphonium, for the fans in the group. Optional.'),
         ('17:30','Back to Kyoto','Evening free.')],
  stops=['Kyoto International Manga Museum','Uji Station Kyoto','Byodoin Temple','Nakamura Tokichi Honten Uji'],
  moves='Museum is central, walkable from most hotels. Kyoto → Uji 30 min by JR. Uji on foot.',
  food=[('Honke Owariya','Kyoto · soba since 1465','The oldest soba house in Kyoto, ten minutes from the museum. Hourai soba with eight toppings in a quiet old townhouse.','Honke Owariya Kyoto'),
        ('Nakamura Tokichi Honten','Uji · matcha','The 1854 tea merchant. Matcha jelly, matcha parfait, and tea to bring home. The garden seats go first.','Nakamura Tokichi Honten Uji')],
  good='Readers. Kyoto Animation fans. Guests who want a calm day between Tokyo and Osaka.',
  mind='The Manga Museum closes Wednesdays. Byodo-in’s Phoenix Hall interior is a timed tour with limited places.',
  links=[('Kyoto International Manga Museum','https://kyotomm.jp/en/'),('Byodo-in','https://www.byodoin.or.jp/en/')]),
 dict(id='6', city='Kyoto → Osaka', chips=['Tezuka museum','Den Den Town','Dotonbori'], name='Tezuka’s hometown, then Osaka', tag='Takarazuka to Den Den Town',
  why='The Tezuka Osamu Manga Museum in Takarazuka, where the author of Astro Boy grew up, then Osaka’s own otaku district, Den Den Town, and Dotonbori street food at night.',
  steps=[('9:30','Luggage forwarded','To the Osaka hotel, arriving the same evening.'),
         ('10:30','Train to Takarazuka','One hour from Kyoto.'),
         ('11:30','Tezuka Osamu Manga Museum','The Phoenix at the entrance, Astro Boy, the animation workshop where you can make a short piece yourself.'),
         ('13:30','Train to Osaka Namba','50 minutes.'),
         ('14:30','Den Den Town and Ota Road','Osaka’s Akihabara: figure shops, retro games, the maid cafes of Nipponbashi.'),
         ('17:30','Dotonbori','Kushikatsu, okonomiyaki, the Glico sign, the canal lights.'),
         ('19:00','Done','Hotel is minutes away.')],
  stops=['Osamu Tezuka Manga Museum Takarazuka','Namba Station Osaka','Nipponbashi Den Den Town Osaka','Dotonbori'],
  moves='Kyoto → Takarazuka 1h by JR. Takarazuka → Namba 50 min. Den Den Town to Dotonbori is a 15-minute walk.',
  food=[('Kushikatsu Daruma Dotonbori','Dotonbori · kushikatsu since 1929','Deep-fried skewers, one dip only in the shared sauce. The angry-chef sign is the landmark.','Kushikatsu Daruma Dotonbori'),
        ('Mizuno','Dotonbori · okonomiyaki since 1945','The yamaimo okonomiyaki cooked on the counter in front of you. Small, and worth the wait.','Mizuno Okonomiyaki Dotonbori')],
  good='Guests who want both the origin story and the loud, delicious side of Osaka.',
  mind='The Tezuka museum is closed Wednesdays. Dotonbori lines are shortest before 18:00.',
  links=[('Tezuka Osamu Manga Museum','https://www.city.takarazuka.hyogo.jp/tezuka/'),('Den Den Town','https://www.nippombashi.jp/')]),
 dict(id='7', city='Osaka', chips=['Two options','USJ or shopping','Departure'], name='USJ, or a shopping finale', tag='Two ways to finish',
  why='Option A is Universal Studios Japan: Super Nintendo World and the seasonal anime collaborations. Option B is a last day for collectors in Nipponbashi, with overseas shipping arranged from the post office. Then Kansai Airport or the train back to Tokyo.',
  steps=[('9:00','Option A: Universal Studios Japan','Early entry for Super Nintendo World. Seasonal collaborations (Jujutsu Kaisen, Detective Conan, Attack on Titan) change every few months.'),
         ('10:00','Option B: collectors’ day','Mandarake Grand Chaos, the Nipponbashi shops, then boxing and shipping purchases home from the post office.'),
         ('15:00','551 Horai','Pork buns at Namba station, the Osaka thing to eat before a train.'),
         ('16:00','Departure','Kansai Airport in 50 minutes by rapid train, or the Shinkansen back to Tokyo in 2 hours 30.')],
  stops=['Universal Studios Japan','Namba Station Osaka','Kansai International Airport'],
  moves='Hotel → USJ 20 min by train. Namba → Kansai Airport 50 min. Namba → Shin-Osaka 15 min for the Shinkansen.',
  food=[('551 Horai Namba','Namba · pork buns','Steamed pork buns made in front of the counter since 1945. Everyone in Osaka carries the white box.','551 Horai Namba Main Store'),
        ('Honke Ohtako','Dotonbori · takoyaki','Big octopus pieces, crisp outside, soft inside, cooked at the stand. Eight for the price of a coffee.','Honke Ohtako Dotonbori')],
  good='Families choose A. Collectors choose B. Both end at the airport on time.',
  mind='USJ Express passes for Nintendo World sell out early. Shipping from Japan Post takes 1 to 2 weeks by air.',
  links=[('Universal Studios Japan','https://www.usj.co.jp/web/en/us')]),
]

def menu(c):
    x = PH[c['id']]['card']
    ch = ''.join(f'<li>{html.escape(t)}</li>' for t in c['chips'])
    return f'''<button class="mcard" type="button" data-course="{c['id']}" aria-expanded="false" aria-controls="detail-{c['id']}">
<img src="{x["thumb"]}" alt="{html.escape(x["title"])}" loading="lazy">
<span class="mb"><span class="mk">Day {c['id']} · {html.escape(c['city'])}</span><span class="mt">{html.escape(c['name'])}</span>
<span class="mtag">{html.escape(c['tag'])}</span><ul class="mch">{ch}</ul><span class="mopen">See the plan</span></span></button>'''

def detail(c):
    ph = ''.join(f'<img src="{x["thumb"]}" alt="{html.escape(x["title"])}" loading="lazy">' for x in PH[c['id']]['detail'])
    st = ''.join(f'<li><b>{t}</b><div><strong>{h}</strong><span>{d}</span></div></li>' for t, h, d in c['steps'])
    fd = ''.join(f'<a class="eat" href="{gm(q)}" target="_blank" rel="noopener">'
                 f'<img src="{im["thumb"]}" alt="{html.escape(im["title"])}" loading="lazy">'
                 f'<span class="eb"><strong>{n}</strong><em>{a}</em><span>{d}</span>'
                 f'<i>Open in Google Maps ↗</i></span></a>'
                 for (n, a, d, q), im in zip(c['food'], PH[c['id']]['food']))
    ln = ' '.join(f'<a href="{u}" target="_blank" rel="noopener">{html.escape(t)} ↗</a>' for t, u in c['links'])
    return f'''<section class="detail" id="detail-{c['id']}" hidden><div class="dwrap"><div class="dtop"></div>
<div class="dhead"><div><p class="kicker">Day {c['id']} · {html.escape(c['city'])} · {html.escape(c['tag'])}</p><h2>{html.escape(c['name'])}</h2></div>
<button class="dclose" type="button" aria-label="Close">Close ✕</button></div>
<p class="why">{html.escape(c['why'])}</p>
<div class="photos">{ph}</div>
<div class="dgrid">
<div><h3>The day</h3><ol class="steps">{st}</ol></div>
<div><h3>The route</h3><div class="mapbox"><iframe src="{route_emb(c['stops'])}" loading="lazy" title="Route for day {c['id']}" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<p class="moves">{c['moves']} <a href="{route_link(c['stops'])}" target="_blank" rel="noopener">Open the route in Google Maps ↗</a></p></div>
</div>
<h3>Where we eat</h3><div class="eats">{fd}</div>
<div class="notes"><p><b>Good for</b> {html.escape(c['good'])}</p><p><b>Keep in mind</b> {html.escape(c['mind'])}</p></div>
<p class="links">{ln}</p>
</div></section>'''

HERO_CSS = """
.hpic{position:relative;background:#111;color:#fff}
.slides{position:absolute;inset:0;overflow:hidden}
.slides img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity 1.1s ease,transform 5s linear}
.slides img.on{opacity:1;transform:scale(1)}
.slides:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.08) 30%,rgba(0,0,0,.74))}
.hcap{position:relative;z-index:1;min-height:62vh;max-height:600px;display:flex;flex-direction:column;justify-content:flex-end;padding-top:48px;padding-bottom:22px}
.hcap .kicker{color:#9ee3b8}
.hcap h1{color:#fff;margin:0 0 14px;text-shadow:0 2px 14px rgba(0,0,0,.3)}
.snav{display:flex;align-items:center;gap:10px}
.slabel{font:inherit;font-size:12.5px;font-weight:600;color:#fff;background:rgba(0,0,0,.38);border:1px solid rgba(255,255,255,.4);border-radius:999px;padding:7px 13px;cursor:pointer;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dots{display:flex;gap:7px;margin-left:auto;flex:none}
.dots button{width:9px;height:9px;padding:0;border:none;border-radius:50%;background:rgba(255,255,255,.45);cursor:pointer}
.dots button.on{background:#fff}
.hbody{padding-top:22px;padding-bottom:26px}
@media(prefers-reduced-motion:reduce){.slides img{transition:none;transform:none}}
"""
HERO_JS = """
 (function(){
  var sl=[].slice.call(document.querySelectorAll('.slides img')),dots=[].slice.call(document.querySelectorAll('.dots button')),lab=document.querySelector('.slabel'),i=0,t;
  function show(n){i=n;sl.forEach(function(x,k){x.classList.toggle('on',k===n)});dots.forEach(function(x,k){x.classList.toggle('on',k===n)});
   lab.textContent='Day '+sl[n].dataset.course+' · '+sl[n].dataset.name;lab.dataset.course=sl[n].dataset.course}
  function go(){clearInterval(t);if(!matchMedia('(prefers-reduced-motion: reduce)').matches)t=setInterval(function(){show((i+1)%sl.length)},4000)}
  dots.forEach(function(d,k){d.addEventListener('click',function(){show(k);go()})});
  lab.addEventListener('click',function(){document.querySelector('.mcard[data-course="'+lab.dataset.course+'"]').click()});
  show(0);go();
 })();
"""

credits = '; '.join(html.escape(x['title'].replace('File:','')) + ' (' + x['lic'] + ')' for v in PH.values() for x in [v['card']] + v['detail'] + v['food'])
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Manga week: Tokyo, Kyoto, Osaka in seven days</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--bg:#fffdf6;--card:#fff;--ink:#111;--mute:#767065;--line:#eae4d6;--acc:#1a5c3a;--r:10px}}
*{{box-sizing:border-box;min-width:0}} html,body{{overflow-x:hidden;max-width:100%}} img{{max-width:100%}}
body{{margin:0;font-family:Inter,-apple-system,"Hiragino Sans",sans-serif;color:var(--ink);background:var(--bg);line-height:1.6}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 20px}}
.kicker{{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin:0 0 10px}}
h1,h2,.mt{{text-wrap:balance}} .nb{{white-space:nowrap}}
h1{{font-weight:800;font-size:clamp(34px,5.4vw,54px);line-height:1.06;letter-spacing:-.025em;margin:0 0 16px}}
h2{{font-weight:800;font-size:clamp(30px,4.2vw,42px);line-height:1.06;letter-spacing:-.025em;margin:0}}
h3{{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin:0 0 12px}}
{HERO_CSS}
header p{{font-size:18px;color:var(--mute);margin:0;max-width:620px}}
.facts{{display:flex;flex-wrap:wrap;gap:6px 20px;margin:20px 0 0;padding:0;list-style:none;font-size:14px;color:var(--mute)}} .facts b{{color:var(--ink);font-weight:600}}
.sechead{{display:flex;align-items:baseline;gap:14px;padding:26px 0 16px;border-top:1px solid var(--line)}}
.sechead .n{{font-weight:800;font-size:26px;line-height:1;letter-spacing:-.02em;color:var(--acc)}}
.sechead b{{font-size:19px;font-weight:600}} .sechead span{{font-size:14px;color:var(--mute)}}
.menu{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}}
.mcard{{display:flex;flex-direction:column;text-align:left;font:inherit;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;padding:0;cursor:pointer;transition:transform .18s,box-shadow .18s,border-color .18s}}
.mcard:hover{{transform:translateY(-3px);box-shadow:0 10px 24px rgba(34,31,27,.10)}}
.menu.picked .mcard:not([aria-expanded=true]){{opacity:.42;filter:saturate(.45)}}
.menu.picked .mcard:not([aria-expanded=true]):hover{{opacity:.75;filter:none}}
.mcard[aria-expanded=true]{{border:2px solid var(--ink);box-shadow:0 12px 28px rgba(17,17,17,.16);transform:translateY(-3px)}}
.mcard[aria-expanded=true] .mopen{{color:var(--acc);border-bottom-color:var(--acc)}}
.mcard>img{{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;background:#f0ebe0}}
.mb{{display:flex;flex-direction:column;flex:1;padding:18px 20px 20px}}
.mk{{display:block;font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin-bottom:6px}}
.mt{{display:block;font-weight:800;font-size:26px;line-height:1.12;letter-spacing:-.025em;margin-bottom:6px}}
.mtag{{display:block;font-size:15px;color:var(--mute);margin-bottom:12px}}
.mch{{list-style:none;margin:auto 0 14px;padding:0;display:flex;flex-wrap:wrap;gap:6px}}
.mch li{{font-size:11px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;border:1px solid var(--line);border-radius:4px;padding:3px 8px;color:var(--mute)}}
.mopen{{align-self:flex-start;display:inline-block;font-size:14px;font-weight:600;border-bottom:2px solid var(--acc);padding-bottom:1px}}
.mcard[aria-expanded=true] .mopen::after{{content:" ▲"}} .mcard[aria-expanded=false] .mopen::after{{content:" ▾"}}
.detail{{scroll-margin-top:12px;display:grid;grid-template-rows:0fr;transition:grid-template-rows .32s ease;margin-top:14px;position:relative}}
.detail[hidden]{{display:none}} .detail.open{{grid-template-rows:1fr}}
.dwrap{{overflow:hidden;min-height:0;background:var(--card);border:2px solid var(--ink);border-radius:var(--r);position:relative}}
.detail::before{{content:'';position:absolute;top:-11px;left:var(--arrow,50%);width:20px;height:20px;margin-left:-10px;background:var(--acc);border-left:2px solid var(--acc);border-top:2px solid var(--acc);transform:rotate(45deg);z-index:2;opacity:0;transition:opacity .2s .12s}}
.detail.open::before{{opacity:1}}
.dtop{{height:5px;background:var(--acc)}}
.detail.open .dwrap{{overflow:visible}}
.dwrap>*{{margin-left:26px;margin-right:26px}} .dwrap>.dtop{{margin:0}} .dwrap>.photos{{margin-left:26px;margin-right:26px}}
.dhead{{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;padding-top:26px}}
.dclose{{flex:none;font:inherit;font-size:12px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--mute);background:none;border:1px solid var(--line);border-radius:6px;padding:8px 14px;cursor:pointer}}
.dclose:hover{{color:var(--ink);border-color:var(--ink)}}
.why{{font-size:17px;color:var(--mute);margin:10px 0 20px;max-width:640px}}
.photos{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-bottom:26px}}
.photos img{{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:8px;background:#f0ebe0}}
.dgrid{{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-bottom:28px}}
.steps{{list-style:none;padding:0;margin:0;border-top:1px solid var(--line)}}
.steps li{{display:grid;grid-template-columns:60px minmax(0,1fr);gap:12px;padding:11px 0;border-bottom:1px solid var(--line)}}
.steps b{{font-variant-numeric:tabular-nums;color:var(--acc);font-weight:600;font-size:14px}} .steps strong{{display:block;font-weight:600;font-size:16px}} .steps span{{color:var(--mute);font-size:14px}}
.mapbox{{border-radius:8px;overflow:hidden;background:#f0ebe0}} .mapbox iframe{{display:block;width:100%;height:300px;border:0}}
.moves{{font-size:14px;color:var(--mute);margin:12px 0 0}} .moves a{{color:var(--ink);text-decoration:underline;text-underline-offset:3px;white-space:nowrap}}
.eats{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-bottom:26px}}
.eat{{display:flex;flex-direction:column;text-decoration:none;color:inherit;background:var(--bg);border:1px solid var(--line);border-radius:8px;overflow:hidden}}
.eat>img{{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;background:#f0ebe0}}
.eb{{display:flex;flex-direction:column;flex:1;padding:14px 16px 16px}}
.eat:hover{{border-color:var(--ink)}}
.eat strong{{display:block;font-weight:700;font-size:18px;line-height:1.2;letter-spacing:-.015em}}
.eat em{{display:block;font-style:normal;font-size:11px;color:var(--acc);font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin:5px 0 9px}}
.eb>span{{display:block;font-size:14px;color:var(--mute)}} .eat i{{display:block;font-style:normal;font-size:12px;margin-top:auto;padding-top:10px;text-decoration:underline;text-underline-offset:3px}}
.notes{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px;font-size:14px}} .notes p{{margin:0;padding:16px 18px;background:var(--bg);border:1px solid var(--line);border-radius:8px}} .notes b{{display:block;font-weight:600;margin-bottom:3px}}
.links{{margin:0 0 22px;font-size:14px;display:flex;flex-wrap:wrap;gap:6px 18px}} .links a{{color:var(--ink);text-decoration:underline;text-underline-offset:3px}}
.choose{{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;font-weight:700;padding:16px 32px;border-radius:8px;font-size:16px;letter-spacing:-.01em;margin-bottom:28px}} .choose:hover{{background:#333}}
.arrival{{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:start;padding-bottom:40px}}
.arrival p{{margin:0 0 10px;font-size:16px}} .arrival .hint{{color:var(--mute);font-size:15px}}
.arrival .mapbox iframe{{height:260px}}
footer.wrap{{padding:26px 20px 60px;font-size:13px;color:var(--mute);border-top:1px solid var(--line)}} footer p{{margin:0 0 6px}}
.cred summary{{cursor:pointer;font-size:12px;color:var(--mute);opacity:.75;list-style:none;display:inline-block;text-decoration:underline;text-underline-offset:3px}}
.cred summary::-webkit-details-marker{{display:none}} .cred p{{margin:8px 0 0;font-size:11.5px;line-height:1.6;opacity:.8}}
@media(max-width:820px){{
 .menu{{grid-template-columns:1fr}} .mcard>img{{aspect-ratio:16/9}}
 .dgrid,.eats,.notes,.arrival,.photos{{grid-template-columns:1fr}}
 .dwrap>*{{margin-left:18px;margin-right:18px}} .mapbox iframe{{height:230px}}
}}
@media(max-width:560px){{
 .wrap{{padding:0 18px}}
 .hcap{{min-height:58vh;padding-bottom:18px}} .hbody{{padding-top:18px;padding-bottom:22px}} .kicker{{margin-bottom:12px}}
 h1{{font-size:33px;line-height:1.08;letter-spacing:-.03em;margin-bottom:14px}}
 header p{{font-size:16px;line-height:1.55;max-width:none}}
 .facts{{display:grid;grid-template-columns:auto 1fr;gap:3px 10px;margin-top:16px;font-size:13px;line-height:1.5}}
 .facts li{{display:contents}} .facts b{{white-space:nowrap}}
 .sechead{{display:block;padding:22px 0 12px}}
 .sechead .n{{font-size:20px;margin-right:8px;display:inline}}
 .sechead b{{font-size:17px}} .sechead span{{display:block;font-size:13px;line-height:1.5;margin-top:2px}}
 .menu{{gap:12px}}
 .mb{{padding:15px 16px 16px}} .mt{{font-size:23px;line-height:1.15}} .mtag{{font-size:14px;margin-bottom:10px}}
 .mch{{gap:5px;margin-bottom:12px}} .mch li{{font-size:10.5px;padding:2px 7px}}
 .mopen{{font-size:13.5px}}
 h2{{font-size:26px;line-height:1.12}}
 .dhead{{padding-top:20px}} .why{{font-size:15.5px;line-height:1.55;margin:8px 0 16px}}
 .dwrap>*{{margin-left:16px;margin-right:16px}}
 .photos{{gap:8px;margin-bottom:20px}} .photos img{{aspect-ratio:3/2}}
 h3{{margin:22px 0 10px}} .dgrid{{gap:0;margin-bottom:0}}
 .steps li{{grid-template-columns:52px minmax(0,1fr);gap:10px;padding:10px 0}}
 .steps strong{{font-size:15.5px}} .steps span{{font-size:13.5px;line-height:1.5}}
 .eats{{gap:10px;margin-bottom:20px}} .eat>img{{aspect-ratio:16/9}} .eb{{padding:12px 14px 14px}}
 .notes{{gap:10px;margin-bottom:16px}} .notes p{{padding:14px 16px;font-size:13.5px}}
 .links{{font-size:13.5px;gap:4px 14px;margin-bottom:18px}}
 .choose{{display:block;text-align:center;padding:15px 0;margin-bottom:22px}}
 .arrival{{gap:16px;padding-bottom:32px}} .arrival p{{font-size:15.5px;line-height:1.55}} .arrival .hint{{font-size:14px}}
 .mapbox iframe{{height:210px}}
 footer.wrap{{padding:20px 18px 44px;font-size:11.5px;line-height:1.55}}
}}
</style></head><body>
<header class="hero">
<div class="hpic"><div class="slides">{''.join(f'<img src="{PH[c["id"]]["card"]["thumb"]}" alt="{html.escape(c["name"])}" data-course="{c["id"]}" data-name="{html.escape(c["name"])}">' for c in DAYS)}</div>
<div class="wrap hcap">
<p class="kicker">Tokyo · Kyoto · Osaka · seven days</p>
<h1>A week of manga, <span class="nb">three cities.</span></h1>
<div class="snav"><button class="slabel" type="button"></button><div class="dots">{''.join(f'<button type="button" aria-label="Show day {c["id"]}"></button>' for c in DAYS)}</div></div>
</div></div>
<div class="wrap hbody">
<p>Seven days built around the places where manga was made and the streets where it lives now. Guided start to finish, luggage forwarded hotel to hotel.</p>
<ul class="facts"><li><b>Guide</b> Yuuki</li><li><b>Days</b> 7</li><li><b>Cities</b> Tokyo → Kyoto → Osaka</li><li><b>Group</b> 2 to 8 guests</li></ul>
</div>
</header>
<div class="wrap">
<div class="sechead"><span class="n">1</span><div><b>The seven days</b> <span>Tap a day to see the plan, the route and where we eat.</span></div></div>
<div class="menu">{''.join(menu(c) for c in DAYS)}</div>
{''.join(detail(c) for c in DAYS)}
<div class="sechead"><span class="n">2</span><div><b>How a departure gets fixed</b> <span>Two things set the calendar; everything else follows.</span></div></div>
<div class="arrival">
<div><p><b>Ghibli Museum tickets</b> go on sale on the 10th of the previous month at 10:00 Japan time and sell out within minutes. Once the target month is known, the trip dates are set around that day and I take care of the purchase.</p>
<p><b>Museum closing days</b> differ by city (Tokiwa-so Mondays, Ghibli Tuesdays, Kyoto Manga Museum and the Tezuka museum Wednesdays). The order of days above already respects them; exact dates are checked again before confirming.</p>
<p class="hint">Shinkansen seats, timed museum entries and luggage forwarding are booked for the whole group in advance. Guests carry a day bag only.</p></div>
<div><p><b>To plan a departure, send me:</b></p>
<ol class="steps"><li><b>1</b><div><strong>Group size and how deep the fandom goes</strong><span>Two collectors and a family of five get different afternoons.</span></div></li>
<li><b>2</b><div><strong>Target months</strong><span>Ghibli tickets decide the exact dates.</span></div></li>
<li><b>3</b><div><strong>Who handles hotels</strong><span>Tokyo (3 nights), Kyoto (2), Osaka (2). Central locations keep every day short.</span></div></li></ol>
<a class="choose" href="mailto:icchan417@gmail.com?subject=Manga%20week%3A%20planning%20a%20departure">Email Yuuki to plan a departure</a></div>
</div>
</div>
<footer class="wrap"><p>This page is safe to share with guests. Times are approximate and move with the day. Booking know-how and the extras stay between Tree and Yuuki.</p>
<details class="cred"><summary>Photo credits</summary><p>{credits}, via Wikimedia Commons.</p></details></footer>
<script>
(function(){{
 var cards=[].slice.call(document.querySelectorAll('.mcard'));
 function close(id,now){{var d=document.getElementById('detail-'+id);d.classList.remove('open');document.querySelector('.menu').classList.remove('picked');if(now){{d.hidden=true;return}}setTimeout(function(){{if(!d.classList.contains('open'))d.hidden=true}},320);
   document.querySelector('.mcard[data-course="'+id+'"]').setAttribute('aria-expanded','false')}}
 function land(id){{var d=document.getElementById('detail-'+id),done=false;function go(){{if(done)return;done=true;d.scrollIntoView({{behavior:'smooth',block:'start'}})}}
   d.addEventListener('transitionend',function f(e){{if(e.target===d){{d.removeEventListener('transitionend',f);go()}}}});setTimeout(go,420)}}
 var menuEl=document.querySelector('.menu');
 function point(id){{var b=document.querySelector('.mcard[data-course="'+id+'"]'),d=document.getElementById('detail-'+id);
   var r=b.getBoundingClientRect(),w=d.getBoundingClientRect();
   d.style.setProperty('--arrow',(r.left+r.width/2-w.left)+'px')}}
 function open_(id){{var d=document.getElementById('detail-'+id);d.hidden=false;menuEl.classList.add('picked');
   requestAnimationFrame(function(){{d.classList.add('open');point(id)}});
   document.querySelector('.mcard[data-course="'+id+'"]').setAttribute('aria-expanded','true')}}
 window.addEventListener('resize',function(){{var o=document.querySelector('.mcard[aria-expanded=true]');if(o)point(o.dataset.course)}});
 var want=(location.hash.match(/^#detail-([1-7])$/)||[])[1]||(location.search.match(/[?&]open=([1-7])/)||[])[1];
 if(want){{open_(want);setTimeout(function(){{document.getElementById('detail-'+want).scrollIntoView()}},80)}}
 cards.forEach(function(b){{
  b.addEventListener('click',function(){{
   var id=b.dataset.course,was=b.getAttribute('aria-expanded')==='true';
   cards.forEach(function(o){{if(o.getAttribute('aria-expanded')==='true')close(o.dataset.course,true)}});
   if(was)return;
   open_(id);history.replaceState(null,'','#detail-'+id);
   land(id);
  }});
 }});
 document.querySelectorAll('.dclose').forEach(function(x){{
  x.addEventListener('click',function(){{var d=x.closest('.detail'),id=d.id.replace('detail-','');close(id);
   document.querySelector('.mcard[data-course="'+id+'"]').scrollIntoView({{behavior:'smooth',block:'center'}})}});
 }});
}})();
{HERO_JS}
</script>
{{DEVBAR}}</body></html>'''
open('index.html', 'w').write(page.replace('{DEVBAR}', ''))
open('preview.html', 'w').write(page.replace(
    '{DEVBAR}',
    '<script>window.DEVBAR_FORCE=1</script><script src="devbar.js?v=3"></script>'))
print('written', len(page), '-> index.html + preview.html')
