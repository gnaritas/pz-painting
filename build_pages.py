#!/usr/bin/env python3
# PZ Painting & Contracting LLC — template-v2 rebuild generator (t_811cd84b, 2026-11-21)
# Every fact on these pages is sourced; see evidence.json. No builder runtime, no third-party JS.
import os, json

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
ORIGIN = "https://pz-painting-demo.up.railway.app"
SITE = "PZ Painting & Contracting, LLC"
SHORT = "PZ Painting"
TEL = "(503) 332-4596"
TELHREF = "+15033324596"
EMAIL = "info@pzpainting.com"
ADDR = "624 Church Street, Woodburn, OR 97071"
LICENSE = "226354"
FB = "https://www.facebook.com/pzpaintingllc/"
OG = ORIGIN + "/og.png"
GMAPS = "https://www.google.com/maps/search/?api=1&query=PZ%20Painting%20%26%20Contracting%2C%20624%20Church%20St%2C%20Woodburn%2C%20OR%2097071"
LAT, LON = "45.1472734", "-122.8576420"

NAV = [("Services", "/services"), ("Client gallery", "/our-work"), ("Contact", "/contact")]

def head(title, desc, path, canonical=True):
    canon = f'<link rel="canonical" href="{ORIGIN}{path}">' if canonical else ""
    return f"""<!doctype html>
<html lang="en">
<!-- BUILT-2026-11-21 -->
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{OG}">
<meta property="og:image:alt" content="PZ Painting & Contracting — residential and commercial painting, Oregon">
<meta property="og:url" content="{ORIGIN}{path}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{OG}">
<meta name="robots" content="noindex, nofollow">
{canon}<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
<link rel="preconnect" href="https://maps.google.com" crossorigin>
<link rel="preconnect" href="https://maps.gstatic.com" crossorigin>
<link rel="preconnect" href="https://www.google.com" crossorigin>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="/">
      <span class="mark">PZ</span>
      <span class="word">PZ Painting<small>&amp; Contracting LLC · Lic# CCB {LICENSE}</small></span>
    </a>
    <nav class="main" aria-label="Main">
      <ul>
{chr(10).join(f'        <li><a href="{href}">{txt}</a></li>' for txt, href in NAV)}
        <li><a class="btn" href="tel:{TELHREF}">{TEL}</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOT = f"""</main>
<footer class="foot">
  <div class="wrap">
    <div class="stroke"></div>
    <div class="footline">
      <a class="brand" href="/"><span class="mark">PZ</span><span class="word">PZ Painting<small>&amp; Contracting LLC</small></span></a>
      <address>
        <a href="tel:{TELHREF}">{TEL}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        {ADDR}
      </address>
      <div class="lic">Oregon CCB License #{LICENSE}<br>
        <a href="{FB}" rel="noopener">Facebook</a> · <a href="/contact">Free quotes</a></div>
      <p class="small">© 2026 {SITE}. Interior &amp; exterior painting, staining, cabinet work and finish carpentry — Woodburn, Oregon and the Portland–Salem corridor.</p>
    </div>
  </div>
</footer>
</body>
</html>
"""

def write(name, html):
    path = os.path.join(OUT, name if name.endswith(".html") else name + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(name, len(html))

# ---------------------------------------------------------------- index
index_ld = json.dumps({
    "@context": "https://schema.org", "@graph": [
        {"@type": "HousePainter", "@id": ORIGIN + "/#business",
         "name": SITE, "url": ORIGIN + "/",
         "telephone": "+1-503-332-4596", "email": EMAIL,
         "image": ORIGIN + "/img/hero.webp",
         "address": {"@type": "PostalAddress", "streetAddress": "624 Church Street",
                     "addressLocality": "Woodburn", "addressRegion": "OR",
                     "postalCode": "97071", "addressCountry": "US"},
         "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
         "licenseNumber": LICENSE,
         "priceRange": "$$",
         "areaServed": [{"@type": "City", "name": n} for n in
                        ["Woodburn", "Portland", "Happy Valley", "Clackamas", "Salem"]],
         "sameAs": [FB],
         "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0",
                             "reviewCount": "4", "bestRating": "5"},
         "makesOffer": [{"@type": "Offer",
                         "itemOffered": {"@type": "Service", "name": n}}
                        for n in ["Interior painting", "Exterior painting",
                                  "Cabinet painting and restoration", "Staining and sealing",
                                  "Gutter and roof servicing", "Finish carpentry",
                                  "Pressure washing", "Small commercial painting"]]},
        {"@type": "FAQPage", "@id": ORIGIN + "/#faq", "mainEntity": [
            {"@type": "Question", "name": "Do you paint homes outside Woodburn?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes — we serve the Portland–Salem corridor: Portland, Happy Valley, Clackamas, Woodburn, Salem and the surrounding areas."}},
            {"@type": "Question", "name": "Is PZ Painting licensed and insured?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes — Oregon CCB Contractor License #226354. The company is licensed, bonded and insured."}},
            {"@type": "Question", "name": "Do you take commercial jobs?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes — residential and commercial: interiors, exteriors, cabinets, staining, sealing and finish carpentry."}},
            {"@type": "Question", "name": "How do I get a price?",
             "acceptedAnswer": {"@type": "Answer", "text": "Every quote is free. Call (503) 332-4596, email info@pzpainting.com, or send the contact form. Personalized options and a wide range of prices cater to every budget."}}]},
        {"@type": "BreadcrumbList", "@id": ORIGIN + "/#bc", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"}]}
    ]}, ensure_ascii=False, indent=1)

index = head("Interior & Exterior House Painters — PZ Painting, Woodburn OR",
    "Residential and commercial painting, staining, cabinets and finish carpentry. Licensed (CCB #226354), bonded, insured. Free quotes — serving Portland to Salem.",
    "/") + f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <p><span class="label">Residential + Commercial Painting · Oregon</span></p>
      <h1>Make it EZ —<br>go <em>with&nbsp;PZ</em></h1>
      <p class="lede">Interior and exterior house painting, cabinet refinishing, staining and finish carpentry — a small crew with a big standard, painting homes from Portland to Salem.</p>
      <div class="badgerow">
        <span class="badge"><b>5.0★</b> Google reviews</span>
        <span class="badge">Licensed · Bonded · Insured</span>
        <span class="badge">CCB&nbsp;#{LICENSE}</span>
        <span class="badge">Family owned &amp; operated</span>
      </div>
      <div class="ctarow">
        <a class="btn" href="/contact">Get a free quote</a>
        <a class="btn ghost" href="tel:{TELHREF}">Call {TEL}</a>
      </div>
    </div>
    <div class="hero-photo">
      <img src="/img/hero.webp" alt="Two-story home freshly painted by PZ Painting & Contracting" width="1300" height="1732">
    </div>
  </div>
</section>

<div class="tape" aria-hidden="true"></div>

<section class="band" aria-labelledby="promise-h">
  <div class="wrap">
    <div class="trustgrid">
      <div class="promise">
        <h3 id="promise-h">“Your project is not over until you are 100% satisfied.”</h3>
      </div>
      <div class="statcard">
        <p class="num">5.0<span class="stars">★</span></p>
        <p>Google rating — Woodburn, OR painter. “Professional, on time, detail-oriented.”</p>
      </div>
      <div class="statcard">
        <p class="num">100%<span class="stars">★</span></p>
        <p>of Facebook visitors recommend this business (11 reviews).</p>
      </div>
    </div>
    <div class="quotegrid">
      <figure class="qcard">
        <span class="stars">★★★★★</span>
        <blockquote>“Ramses and his crew are very professional and pay attention to detail… they definitely delivered on every aspect we anticipated!”</blockquote>
        <cite>Athena M. · Google review · exterior paint</cite>
      </figure>
      <figure class="qcard">
        <span class="stars">★★★★★</span>
        <blockquote>“From the moment we reached out, Ramses was prompt and professional with his communication… Our home in Happy Valley was in serious need of trim repair…”</blockquote>
        <cite>Berta A. · Google review · trim repair</cite>
      </figure>
      <figure class="qcard">
        <span class="stars">★★★★★</span>
        <blockquote>“Ramses did an amazing job on our cabinets! Highly recommend! Not only are they fast &amp; efficient they pay close attention to detail.”</blockquote>
        <cite>Candice R. · Google review · cabinets</cite>
      </figure>
    </div>
  </div>
</section>

<section class="band paper2" aria-labelledby="svc-h">
  <div class="wrap">
    <div class="secthead">
      <p><span class="label">What we paint</span></p>
      <h2 id="svc-h">One crew, every coat</h2>
      <p>“Clients can consistently expect a solid commitment to quality, strong work ethic, and punctuality. Our personalized options and wide range of prices cater to every budget.” — from the PZ promise, straight from their own words.</p>
    </div>
    <div class="fan">
      <a class="svc chip-navy" href="/interior-painting"><span class="swatch"></span><h3>Interior Painting</h3><p>Rooms, hallways, ceilings, trim and doors.</p></a>
      <a class="svc chip-sage" href="/exterior-painting"><span class="swatch"></span><h3>Exterior Painting</h3><p>Siding, trim, soffits, fascia and porches.</p></a>
      <a class="svc chip-teal" href="/interior-painting"><span class="swatch"></span><h3>Cabinet Painting + Restoration</h3><p>Kitchen and bath cabinets — painted or restored.</p></a>
      <a class="svc chip-sand" href="/exterior-painting"><span class="swatch"></span><h3>Staining + Sealing</h3><p>Decks, fences and bare wood, stained and sealed.</p></a>
      <a class="svc chip-slate" href="/exterior-painting"><span class="swatch"></span><h3>Gutter + Roof Servicing</h3><p>Gutter cleanout and roof-debris servicing.</p></a>
      <a class="svc chip-stone" href="/interior-painting"><span class="swatch"></span><h3>Finish Carpentry</h3><p>Trim, base, casing and millwork.</p></a>
      <a class="svc chip-terra" href="/exterior-painting"><span class="swatch"></span><h3>Pressure Washing</h3><p>Exteriors, decks, driveways and walkways.</p></a>
      <a class="svc chip-gold" href="/services"><span class="swatch"></span><h3>Small Commercial</h3><p>Stores, offices and tenant spaces.</p></a>
    </div>
    <p class="more"><a class="btn ghost" href="/services">All services</a></p>
  </div>
</section>

<div class="stroke" aria-hidden="true"></div>

<section class="band" aria-labelledby="work-h">
  <div class="wrap">
    <div class="secthead">
      <p><span class="label">Client gallery</span></p>
      <h2 id="work-h">The work speaks first</h2>
      <p>Photos from client projects — the crew’s own before-the-rebuild gallery, exteriors to cabinets.</p>
    </div>
    <div class="workgrid">
      <figure class="work"><img src="/img/ext-ladder.webp" alt="Client exterior project — ladders set against a stone and siding two-story home" width="680" height="850"><span class="tag">Exterior</span></figure>
      <figure class="work"><img src="/img/ext-garage.webp" alt="Client exterior project — two-story home with garage" width="640" height="644"><span class="tag">Exterior</span></figure>
      <figure class="work"><img src="/img/kitchen.webp" alt="Client cabinet project — refinished kitchen cabinets with blue island" width="680" height="907"><span class="tag">Cabinets</span></figure>
    </div>
    <p class="more"><a class="btn" href="/our-work">See the full gallery</a></p>
  </div>
</section>

<section class="band reband onred" aria-labelledby="support-h" style="background:var(--red)">
  <div class="wrap" style="text-align:center">
    <h2 id="support-h" style="font-family:var(--disp);text-transform:uppercase;font-weight:800;font-size:clamp(24px,3.2vw,38px);letter-spacing:.06em">Support small · Support local · Support family owned</h2>
  </div>
</section>

<section class="band paper2" aria-labelledby="area-h">
  <div class="wrap">
    <div class="areagrid">
      <div class="areacopy">
        <div class="secthead" style="margin-bottom:6px">
          <p><span class="label">Service area</span></p>
          <h2 id="area-h">Woodburn based.<br>Portland to Salem.</h2>
        </div>
        <p>Registered in Woodburn and painting homes across the valley — reviews put the crew at work from Portland and Happy Valley to Clackamas.</p>
        <div class="citychips">
          <span class="city">Woodburn</span><span class="city">Portland</span><span class="city">Happy Valley</span><span class="city">Clackamas</span><span class="city">Salem</span><span class="city">+ surrounding areas</span>
        </div>
        <ul class="num-list">
          <li>Free quotes on every project — residential and commercial.</li>
          <li>“We only mark up a product when it comes to labor to keep our customers happy!”</li>
        </ul>
      </div>
      <div class="mapwrap">
        <iframe title="Map — PZ Painting & Contracting, {ADDR}" src="https://www.google.com/maps?q={LAT},{LON}&amp;z=13&amp;output=embed" loading="lazy"></iframe>
      </div>
    </div>
  </div>
</section>

<section class="callband onink">
  <div class="wrap">
    <div class="inner">
      <div>
        <h2>Ready for a fresh coat?</h2>
        <p>Tell us about the room, the house or the cabinets — quotes are always free.</p>
      </div>
      <div class="ctarow">
        <a class="btn" href="/contact">Free quote form</a>
        <a class="btn ghost" href="tel:{TELHREF}">{TEL}</a>
      </div>
    </div>
  </div>
</section>

<section class="band" aria-labelledby="faq-h">
  <div class="wrap">
    <div class="secthead">
      <p><span class="label">Common questions</span></p>
      <h2 id="faq-h">Before you call</h2>
    </div>
    <div class="faq">
      <details><summary>Do you paint homes outside Woodburn?</summary><p>Yes — we serve the Portland–Salem corridor: Portland, Happy Valley, Clackamas, Woodburn, Salem and the surrounding areas.</p></details>
      <details><summary>Is PZ Painting licensed and insured?</summary><p>Yes — Oregon CCB Contractor License #{LICENSE}. The company is licensed, bonded and insured.</p></details>
      <details><summary>Do you take commercial jobs?</summary><p>Yes — residential and commercial: interiors, exteriors, cabinets, staining, sealing and finish carpentry.</p></details>
      <details><summary>How do I get a price?</summary><p>Every quote is free. Call {TEL}, email <a href="mailto:{EMAIL}">{EMAIL}</a>, or send the contact form. Personalized options and a wide range of prices cater to every budget.</p></details>
    </div>
  </div>
</section>

<script type="application/ld+json">
{index_ld}
</script>
""" + FOOT
write("index", index)

# ---------------------------------------------------------------- services
services_ld = json.dumps({
    "@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Services", "item": ORIGIN + "/services"}]},
        {"@type": "Service", "name": "Residential & Commercial Painting Services",
         "provider": {"@id": ORIGIN + "/#business"},
         "serviceType": "Painting, staining, cabinet refinishing and finish carpentry",
         "areaServed": "Portland–Salem corridor, Oregon"}
    ]}, ensure_ascii=False, indent=1)

services = head("Painting & Contracting Services — PZ Painting, Woodburn OR",
    "Interior and exterior painting, cabinets, staining, gutter and roof servicing, pressure washing, finish carpentry and small commercial work. Free quotes.",
    "/services") + f"""
<section class="minihead">
  <div class="wrap">
    <p><span class="label">Services</span></p>
    <h1>Everything under<br>one scaffold</h1>
    <p class="lede">Painting, staining, cabinet work and the carpentry that goes with it — booked as one crew, not a parade of subcontractors.</p>
  </div>
  <div class="photochip"><img src="/img/ext-ladder.webp" alt="" aria-hidden="true"></div>
</section>

<section class="band">
  <div class="wrap">
    <div class="secthead">
      <p><span class="label">The service deck</span></p>
      <h2>Pick your coats</h2>
      <p>“Clients can consistently expect a solid commitment to quality, strong work ethic, and punctuality. Our personalized options and wide range of prices cater to every budget.”</p>
    </div>
    <div class="fan">
      <a class="svc chip-navy" href="/interior-painting"><span class="swatch"></span><h3>Interior Painting</h3><p>Rooms, hallways, ceilings, trim and doors.</p></a>
      <a class="svc chip-sage" href="/exterior-painting"><span class="swatch"></span><h3>Exterior Painting</h3><p>Siding, trim, soffits, fascia and porches.</p></a>
      <a class="svc chip-teal" href="/interior-painting"><span class="swatch"></span><h3>Cabinet Painting + Restoration</h3><p>Kitchen and bath cabinets — painted or restored.</p></a>
      <a class="svc chip-sand" href="/exterior-painting"><span class="swatch"></span><h3>Staining + Sealing</h3><p>Decks, fences and bare wood, stained and sealed.</p></a>
      <a class="svc chip-slate" href="/exterior-painting"><span class="swatch"></span><h3>Gutter + Roof Servicing</h3><p>Gutter cleanout and roof-debris servicing.</p></a>
      <a class="svc chip-stone" href="/interior-painting"><span class="swatch"></span><h3>Finish Carpentry</h3><p>Trim, base, casing and millwork.</p></a>
      <a class="svc chip-terra" href="/exterior-painting"><span class="swatch"></span><h3>Pressure Washing</h3><p>Exteriors, decks, driveways and walkways.</p></a>
      <a class="svc chip-gold" href="/contact"><span class="swatch"></span><h3>Small Commercial</h3><p>Stores, offices and tenant spaces — ask for a free quote.</p></a>
    </div>
  </div>
</section>

<section class="callband onink">
  <div class="wrap">
    <div class="inner">
      <div>
        <h2>Not sure which service you need?</h2>
        <p>Snap a photo, describe the project, and we’ll walk it with you. Quotes are free.</p>
      </div>
      <div class="ctarow">
        <a class="btn" href="/contact">Free quote form</a>
        <a class="btn ghost" href="tel:{TELHREF}">{TEL}</a>
      </div>
    </div>
  </div>
</section>

<script type="application/ld+json">
{services_ld}
</script>
""" + FOOT
write("services", services)

# ---------------------------------------------------------------- exterior
ext_ld = json.dumps({
    "@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Services", "item": ORIGIN + "/services"},
            {"@type": "ListItem", "position": 3, "name": "Exterior Painting & Staining", "item": ORIGIN + "/exterior-painting"}]},
        {"@type": "Service", "name": "Exterior Painting, Staining & Pressure Washing",
         "provider": {"@id": ORIGIN + "/#business"},
         "serviceType": "Exterior painting, staining and sealing, gutter and roof servicing, pressure washing",
         "areaServed": [{"@type": "City", "name": n} for n in ["Woodburn", "Portland", "Clackamas", "Salem"]]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": "What does exterior painting include?",
             "acceptedAnswer": {"@type": "Answer", "text": "Siding, trim, soffits, fascia and porches — stained or painted. The crew also handles the pressure washing and gutter and roof servicing that go with it."}},
            {"@type": "Question", "name": "Do you stain decks and fences too?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes — staining and sealing for decks, fences and bare wood is part of the service menu."}}]},
    ]}, ensure_ascii=False, indent=1)

ext = head("Exterior Painting, Staining & Washing — PZ Painting, Clackamas OR",
    "Exterior house painting, deck and fence staining, pressure washing and gutter servicing. Licensed CCB #226354. Free quotes from Woodburn to Portland and Salem.",
    "/exterior-painting") + f"""
<section class="minihead">
  <div class="wrap">
    <p><span class="label">Exterior services</span></p>
    <h1>Curb appeal,<br>coat by coat</h1>
    <p class="lede">Exterior painting, staining and sealing, pressure washing and gutter servicing — the whole outside, handled by one licensed crew.</p>
  </div>
  <div class="photochip"><img src="/img/ext-row.webp" alt="" aria-hidden="true"></div>
</section>

<section class="band">
  <div class="wrap">
    <div class="secthead">
      <p><span class="label">Exterior painting + staining</span></p>
      <h2>What the outside gets</h2>
    </div>
    <div class="areagrid">
      <div>
        <ul class="num-list" style="margin-top:0">
          <li><strong>Exterior painting</strong> — siding, trim, soffits, fascia and porches.</li>
          <li><strong>Staining + sealing</strong> — decks, fences and bare wood protected against the wet season.</li>
          <li><strong>Pressure washing</strong> — house exteriors, decks, driveways and walkways, cleaned before the new coat goes on.</li>
          <li><strong>Gutter + roof servicing</strong> — gutters cleared and roof debris off, done alongside the paint work.</li>
        </ul>
        <div class="ctarow" style="margin-top:24px">
          <a class="btn" href="/contact">Free exterior quote</a>
          <a class="btn ghost" href="tel:{TELHREF}">{TEL}</a>
        </div>
      </div>
      <div>
        <figure class="work"><img src="/img/powerwash.webp" alt="Pressure washing stone steps outside a client home" width="720" height="480"><span class="tag">In progress</span></figure>
      </div>
    </div>
  </div>
</section>

<section class="band paper2">
  <div class="wrap">
    <div class="workgrid">
      <figure class="work"><img src="/img/ext-ladder.webp" alt="Client exterior project — ladders against a stone and siding two-story" width="680" height="850"><span class="tag">Exterior</span></figure>
      <figure class="work"><img src="/img/ext-garage.webp" alt="Client exterior project — two-story home with garage" width="640" height="644"><span class="tag">Exterior</span></figure>
      <figure class="work"><img src="/img/gutter.webp" alt="Cleaning gutter debris off a client roofline" width="720" height="480"><span class="tag">Gutters</span></figure>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="secthead">
      <p><span class="label">Exterior questions</span></p>
      <h2>Good to know</h2>
    </div>
    <div class="faq">
      <details><summary>What does exterior painting include?</summary><p>Siding, trim, soffits, fascia and porches — stained or painted. The crew also handles the pressure washing and gutter and roof servicing that go with it.</p></details>
      <details><summary>Do you stain decks and fences too?</summary><p>Yes — staining and sealing for decks, fences and bare wood is part of the service menu.</p></details>
    </div>
  </div>
</section>

<section class="callband onink">
  <div class="wrap">
    <div class="inner">
      <div>
        <h2>Paint the outside right</h2>
        <p>Serving Portland to Salem — Woodburn, Happy Valley, Clackamas and surrounding areas.</p>
      </div>
      <div class="ctarow">
        <a class="btn" href="/contact">Free quote form</a>
        <a class="btn ghost" href="tel:{TELHREF}">{TEL}</a>
      </div>
    </div>
  </div>
</section>

<script type="application/ld+json">
{ext_ld}
</script>
""" + FOOT
write("exterior-painting", ext)

# ---------------------------------------------------------------- interior
int_ld = json.dumps({
    "@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Services", "item": ORIGIN + "/services"},
            {"@type": "ListItem", "position": 3, "name": "Interior & Cabinet Painting", "item": ORIGIN + "/interior-painting"}]},
        {"@type": "Service", "name": "Interior & Cabinet Painting with Finish Carpentry",
         "provider": {"@id": ORIGIN + "/#business"},
         "serviceType": "Interior painting, cabinet painting and restoration, finish carpentry",
         "areaServed": [{"@type": "City", "name": n} for n in ["Woodburn", "Portland", "Happy Valley", "Salem"]]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": "Can you paint kitchen cabinets?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes — cabinet painting and restoration is one of the crew’s signature services. A Happy Valley client: “Ramses did an amazing job on our cabinets! Highly recommend!”"}},
            {"@type": "Question", "name": "Do you handle trim repair with the paint?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes — finish carpentry (trim, base, casing and millwork) is on the service menu, so rotten or damaged trim gets repaired before it gets painted."}}]},
    ]}, ensure_ascii=False, indent=1)

int = head("Interior & Cabinet Painting — PZ Painting, Happy Valley OR",
    "Interior house painting, kitchen cabinet refinishing and restoration, and finish carpentry. Five-star rated. Free quotes — Portland, Happy Valley, Woodburn, Salem.",
    "/interior-painting") + f"""
<section class="minihead">
  <div class="wrap">
    <p><span class="label">Interior services</span></p>
    <h1>Rooms that look<br>brand new</h1>
    <p class="lede">Interior painting, cabinet refinishing and restoration, and the finish carpentry that makes the paint lines clean.</p>
  </div>
  <div class="photochip"><img src="/img/kitchen.webp" alt="" aria-hidden="true"></div>
</section>

<section class="band">
  <div class="wrap">
    <div class="secthead">
      <p><span class="label">Interior painting + cabinets</span></p>
      <h2>What the inside gets</h2>
    </div>
    <div class="areagrid">
      <div>
        <ul class="num-list" style="margin-top:0">
          <li><strong>Interior painting</strong> — rooms, hallways, ceilings, trim and doors.</li>
          <li><strong>Cabinet painting + restoration</strong> — kitchen and bath cabinets, painted or restored.</li>
          <li><strong>Finish carpentry</strong> — trim, base, casing and millwork repaired or installed before the coat goes on.</li>
          <li><strong>Small commercial</strong> — stores, offices and tenant spaces welcome too.</li>
        </ul>
        <div class="ctarow" style="margin-top:24px">
          <a class="btn" href="/contact">Free interior quote</a>
          <a class="btn ghost" href="tel:{TELHREF}">{TEL}</a>
        </div>
      </div>
      <div>
        <figure class="work"><img src="/img/kitchen.webp" alt="Refinished kitchen cabinets in white with a blue island" width="680" height="907"><span class="tag">Client kitchen</span></figure>
      </div>
    </div>
  </div>
</section>

<section class="band paper2">
  <div class="wrap">
    <div class="workgrid">
      <figure class="work"><img src="/img/bedroom.webp" alt="Client bedroom project — freshly painted walls with dark accent wall" width="680" height="513"><span class="tag">Interior</span></figure>
      <figure class="work"><img src="/img/hall.webp" alt="Client interior project — hallway painted in dark green" width="680" height="680"><span class="tag">Interior</span></figure>
      <figure class="work"><img src="/img/kitchen.webp" alt="Client cabinet project — refinished cabinets with blue island" width="680" height="907"><span class="tag">Cabinets</span></figure>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="secthead">
      <p><span class="label">Interior questions</span></p>
      <h2>Good to know</h2>
    </div>
    <div class="faq">
      <details><summary>Can you paint kitchen cabinets?</summary><p>Yes — cabinet painting and restoration is one of the crew’s signature services. A Happy Valley client: “Ramses did an amazing job on our cabinets! Highly recommend!”</p></details>
      <details><summary>Do you handle trim repair with the paint?</summary><p>Yes — finish carpentry (trim, base, casing and millwork) is on the service menu, so rotten or damaged trim gets repaired before it gets painted.</p></details>
    </div>
  </div>
</section>

<section class="callband onink">
  <div class="wrap">
    <div class="inner">
      <div>
        <h2>New color? New cabinets?</h2>
        <p>One crew for the paint and the carpentry — serving Portland to Salem.</p>
      </div>
      <div class="ctarow">
        <a class="btn" href="/contact">Free quote form</a>
        <a class="btn ghost" href="tel:{TELHREF}">{TEL}</a>
      </div>
    </div>
  </div>
</section>

<script type="application/ld+json">
{int_ld}
</script>
""" + FOOT
write("interior-painting", int)

# ---------------------------------------------------------------- our work
work_ld = json.dumps({
    "@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Client gallery", "item": ORIGIN + "/our-work"}]},
        {"@type": "CollectionPage", "name": "Client Gallery", "url": ORIGIN + "/our-work",
         "isPartOf": {"@id": ORIGIN + "/#business"}}
    ]}, ensure_ascii=False, indent=1)

work = head("Client Gallery — PZ Painting & Contracting, Woodburn OR",
    "Photos from PZ Painting client projects: exterior repaints, kitchens and cabinets, hallways and bedrooms — around the Portland–Salem corridor.",
    "/our-work") + f"""
<section class="minihead">
  <div class="wrap">
    <p><span class="label">Client gallery</span></p>
    <h1>The work<br>speaks first</h1>
    <p class="lede">Exteriors, interiors and cabinets — photos from client projects shared by the crew.</p>
  </div>
  <div class="photochip"><img src="/img/ext-garage.webp" alt="" aria-hidden="true"></div>
</section>

<section class="band">
  <div class="wrap">
    <div class="workgrid">
      <figure class="work"><img src="/img/ext-ladder.webp" alt="Client exterior project — ladders against a stone and siding two-story" width="680" height="850"><span class="tag">Exterior</span></figure>
      <figure class="work"><img src="/img/ext-garage.webp" alt="Client exterior project — two-story home with garage" width="640" height="644"><span class="tag">Exterior</span></figure>
      <figure class="work"><img src="/img/ext-row.webp" alt="Client exterior project — two row homes with gabled roofs" width="680" height="680"><span class="tag">Exterior</span></figure>
      <figure class="work"><img src="/img/kitchen.webp" alt="Client cabinet project — refinished cabinets with blue island" width="680" height="907"><span class="tag">Cabinets</span></figure>
      <figure class="work"><img src="/img/bedroom.webp" alt="Client bedroom project — freshly painted walls with dark accent wall" width="680" height="513"><span class="tag">Interior</span></figure>
      <figure class="work"><img src="/img/hall.webp" alt="Client interior project — hallway painted in dark green" width="680" height="680"><span class="tag">Interior</span></figure>
    </div>
  </div>
</section>

<section class="callband onink">
  <div class="wrap">
    <div class="inner">
      <div>
        <h2>Want your house in the next gallery?</h2>
        <p>Quotes are free — call, email or send the form.</p>
      </div>
      <div class="ctarow">
        <a class="btn" href="/contact">Free quote form</a>
        <a class="btn ghost" href="tel:{TELHREF}">{TEL}</a>
      </div>
    </div>
  </div>
</section>

<script type="application/ld+json">
{work_ld}
</script>
""" + FOOT
write("our-work", work)

# ---------------------------------------------------------------- contact
contact = head("Free Quotes — PZ Painting & Contracting, Woodburn OR",
    "Contact PZ Painting & Contracting for a free quote: call (503) 332-4596, email, or send the form. Licensed Oregon contractor CCB #226354 — Woodburn, OR.",
    "/contact") + f"""
<section class="minihead">
  <div class="wrap">
    <p><span class="label">Contact</span></p>
    <h1>Get a free quote</h1>
    <p class="lede">Tell us about the room, the house or the cabinets. Quotes are always free — and the first call costs nothing.</p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="contactgrid">
      <form class="cform" method="post" action="/contact">
        <label>Name *<input name="name" required autocomplete="name" placeholder="Your name"></label>
        <label>Phone<input name="phone" type="tel" autocomplete="tel" placeholder="(503) 555-0134"></label>
        <label>Email<input name="email" type="email" autocomplete="email" placeholder="you@example.com"></label>
        <label>Best day to reach you<input name="callback" autocomplete="off" placeholder="e.g. weekday mornings"></label>
        <label class="full">About the project *<textarea name="message" required placeholder="House exterior, kitchen cabinets, a bedroom or two…"></textarea></label>
        <input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button class="btn" type="submit">Send it over</button>
      </form>
      <div class="info">
        <h3>Or reach us direct</h3>
        <div class="row"><b>Call</b><a href="tel:{TELHREF}">{TEL}</a></div>
        <div class="row"><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div class="row"><b>Find us</b>{ADDR}</div>
        <div class="row"><b>Licensed</b>Oregon CCB #{LICENSE}</div>
        <div class="row"><b>Serving</b>Portland · Happy Valley · Clackamas · Woodburn · Salem</div>
        <p class="fine">“Your project is not over until you are 100% satisfied!”</p>
      </div>
    </div>
    <div class="mapwrap" style="margin-top:26px">
      <iframe title="Map — PZ Painting & Contracting, {ADDR}" src="https://www.google.com/maps?q={LAT},{LON}&amp;z=13&amp;output=embed" loading="lazy"></iframe>
    </div>
  </div>
</section>

<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"ContactPage","name":"Free Quotes — {SITE}","url":"{ORIGIN}/contact","isPartOf":{{"@id":"{ORIGIN}/#business"}}}}
</script>
""" + FOOT
write("contact", contact)

# ---------------------------------------------------------------- privacy
privacy = head("Privacy — PZ Painting & Contracting, Woodburn OR",
    "How this site handles information: no cookies, no tracking scripts, no analytics. Quote-form details go to the shop's inbox only.",
    "/privacy") + f"""
<section class="band util prose">
  <div class="wrap">
    <p><span class="label">Privacy</span></p>
    <h1>Privacy in plain English</h1>
    <p>This site sets no cookies and loads no analytics or advertising scripts. Your browser contacts this site and, if you open the map or a link to Facebook, the service you requested — nothing else runs in the background.</p>
    <h2>What we collect</h2>
    <p>If you send the quote form, the details you type (name, phone, email and your message) are delivered to {SITE}’s inbox so the shop can answer your quote request. Nothing else about your visit is stored by the site itself.</p>
    <h2>Third-party links</h2>
    <p>The page links to Facebook and Google Maps, which have their own privacy policies. The crew’s Facebook page: <a href="{FB}" rel="noopener">facebook.com/pzpaintingllc</a>.</p>
    <h2>Questions</h2>
    <p>Call {TEL} or email <a href="mailto:{EMAIL}">{EMAIL}</a> anytime. You can also reply to any message you received and ask for it to be stopped.</p>
    <p>Effective date: November 21, 2026.</p>
  </div>
</section>

<script type="application/ld+json">
{json.dumps({"@context":"https://schema.org","@graph":[
  {"@type":"WebPage","@id":ORIGIN+"/privacy","name":"Privacy — "+SITE,"url":ORIGIN+"/privacy","inLanguage":"en","about":{"@id":ORIGIN+"/#business"}},
  {"@type":"BreadcrumbList","itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":ORIGIN+"/"},
    {"@type":"ListItem","position":2,"name":"Privacy","item":ORIGIN+"/privacy"}]}
]}, ensure_ascii=False, indent=1)}
</script>
""" + FOOT
write("privacy", privacy)

# ---------------------------------------------------------------- thanks / 404
thanks = head("Quote request sent — PZ Painting & Contracting",
    "Your quote request is on its way to PZ Painting & Contracting. For anything urgent, call (503) 332-4596.",
    "/thanks") + f"""
<section class="band util">
  <div class="wrap">
    <p><span class="label">Sent</span></p>
    <h1>Request received</h1>
    <p>Thanks — your project note is on its way to the crew. For anything urgent, call <a href="tel:{TELHREF}">{TEL}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <p style="margin-top:22px"><a class="btn ghost" href="/">Back to the home page</a></p>
  </div>
</section>
""" + FOOT
write("thanks", thanks)

e404 = head("Page not found — PZ Painting & Contracting",
    "That page isn't here. Head back to PZ Painting & Contracting's home page for services, gallery and free quotes.",
    "/404") + f"""
<section class="band util">
  <div class="wrap">
    <p><span class="label">404</span></p>
    <h1>That page isn’t here</h1>
    <p>Check the link or start over from the home page — services, gallery and the free-quote form are all one click away.</p>
    <p style="margin-top:22px"><a class="btn" href="/">Take me home</a></p>
  </div>
</section>
""" + FOOT
write("404", e404)

# ---------------------------------------------------------------- sitemap
PAGES = ["", "services", "exterior-painting", "interior-painting", "our-work", "contact", "privacy"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in PAGES:
    sm += f"  <url><loc>{ORIGIN}/{p}</loc></url>\n"
sm += "</urlset>\n"
with open(os.path.join(OUT, "sitemap.xml"), "w") as f: f.write(sm)
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: " + ORIGIN + "/sitemap.xml\n")
print("sitemap + robots written")
