import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ─── EMAIL ────────────────────────────────────────────────────────────────────
def send_inquiry_email(name, email, org, service, message):
    try:
        sender    = st.secrets["EMAIL_ADDRESS"]
        password  = st.secrets["EMAIL_PASSWORD"]
        recipient = "faraimupfuti@gmail.com"
        msg = MIMEMultipart("alternative")
        msg["Subject"]  = f"New Afrogenomics Inquiry — {service}"
        msg["From"]     = sender
        msg["To"]       = recipient
        msg["Reply-To"] = email
        body = f"New inquiry:\n\nName: {name}\nEmail: {email}\nOrganisation: {org or 'Not provided'}\nService: {service}\n\nMessage:\n{message}".strip()
        msg.attach(MIMEText(body, "plain"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        return True
    except Exception:
        return False

# ─── LANGUAGE CONTENT ─────────────────────────────────────────────────────────
LANG = {
    "EN": {
        "flag": "🇬🇧", "label": "EN",
        "eyebrow": "🧬 Bioinformatics Consultancy · Harare, Zimbabwe",
        "hero_title": "Turning raw sequencing data into answers for African research.",
        "hero_sub": "We build the analysis pipelines, infrastructure, and interpretation that African research institutions, universities, and diagnostics labs need — without the cost or delay of outsourcing analysis overseas.",
        "hero_cta": "Book a free consultation →",
        "hero_ghost": "View services",
        "stat1_num": "10+", "stat1_label": "Pipeline & ML projects delivered",
        "stat2_num": "MSc", "stat2_label": "Bioinformatics, University of Tübingen",
        "stat3_num": "2–4 wks", "stat3_label": "Typical turnaround on a pipeline project",
        "stat4_num": "Local", "stat4_label": "Analysis, instead of outsourcing to SA/EU",
        "how_label": "Process", "how_title": "How it works",
        "how_sub": "Three steps from first contact to results in your hands.",
        "steps": [
            ("01", "Tell us what you have and what you need",
             "Share your sequencing data or a description of it, your research question, and your deadline. No technical jargon required — we ask the right questions to scope the work correctly."),
            ("02", "We agree a fixed deliverable before any work begins",
             "You receive a short written scope: exactly what we will analyse, what you will receive, the timeline, and the cost. No surprises. You only proceed when you are satisfied."),
            ("03", "Receive your results, explained clearly",
             "We deliver your report, annotated results, or trained model with a plain-language summary of what the findings mean for your research. Follow-up questions included at no extra charge."),
        ],
        "serve_label": "Who we help", "serve_title": "Who we serve",
        "serve_sub": "We work with any organisation that generates biological data and needs expert analysis to make sense of it.",
        "clients": [
            ("🏥", "Research Institutes", "HIV, TB, and NTD programmes with active genomic surveillance or drug-resistance monitoring needs — such as BRTI and KEMRI-affiliated groups."),
            ("🎓", "Universities & Academia", "Research groups at UZ, NUST, HIT, and regional universities that generate sequencing data but lack in-house bioinformatics staff or compute infrastructure."),
            ("🌍", "NGOs & Global Health Orgs", "PEPFAR-funded programmes, Wellcome Trust projects, and Gates Foundation-backed initiatives needing local African bioinformatics capacity as a subcontract or partner."),
            ("🧪", "Diagnostics Labs", "Private and public labs scaling up to offer genomic testing services — variant-based diagnosis, pharmacogenomics — who need pipeline infrastructure but not a full in-house team."),
            ("🌱", "Agricultural Research", "Crop genomics and disease-resistance profiling for commercial farms, seed companies, and agricultural research bodies across Zimbabwe and the SADC region."),
            ("💊", "Pharma & Biotech", "Companies and CROs needing African-population genomic analysis, NTD drug target work, or bioinformatics support for clinical trial datasets."),
        ],
        "svc_label": "What we offer", "svc_title": "Services",
        "svc_sub": "Each engagement is fixed-scope with a clear deliverable — you know exactly what you are getting before work begins.",
        "services": [
            {"icon":"🔬","title":"Genomic Analysis Pipelines","who":"For labs with sequencing data sitting unanalysed",
             "desc":"You send us your raw sequencing files. We build an automated, reproducible workflow, run your data through it, and return clean annotated results — ready to use in a paper or report. No more waiting months for overseas analysis.",
             "price":"From $2,000 / project","badge":None},
            {"icon":"🧬","title":"Variant Calling & Resistance Reporting","who":"For HIV, TB, and infectious disease research groups",
             "desc":"We take your raw sequencing output and return a clearly formatted report identifying every mutation and flagging those with known drug-resistance implications — ready for clinical or research use.",
             "price":"From $1,200 / cohort","badge":None},
            {"icon":"🤖","title":"AI-Powered Genomic Prediction","who":"For researchers who need more than a standard analysis",
             "desc":"When your question goes beyond identifying mutations — predicting treatment response, identifying which drugs might work against a new pathogen, or finding patterns across a clinical dataset — we build a custom AI model and deliver an interpretable, actionable output.",
             "price":"Scoped per project","badge":None},
            {"icon":"🎓","title":"Training & Capacity Building","who":"For universities, institutes, and lab teams",
             "desc":"Your team collects the data — we teach them to analyse it. Practical hands-on workshops in genomic data analysis, delivered on-site in Harare or remotely. Attendees leave with working skills they can apply immediately.",
             "price":"From $300 / participant","badge":None},
            {"icon":"💊","title":"Drug Target & Repurposing Analysis","who":"For NTD, HIV, and TB research programs",
             "desc":"We computationally identify which existing approved drugs have potential against your target, using AI-predicted protein structures and molecular screening. Faster and far cheaper than starting drug discovery from scratch.",
             "price":"Scoped per project","badge":None},
            {"icon":"🦠","title":"Gut & Environmental Microbiome Analysis","who":"For clinical and environmental research groups",
             "desc":"We analyse your sequencing data and return a full report with species composition, diversity metrics, and group comparisons. Reference databases calibrated for African populations.",
             "price":"From $1,800 / project","badge":"coming_soon"},
            {"icon":"🔄","title":"Ongoing Research Support","who":"For active labs that need a bioinformatician on call",
             "desc":"A dedicated monthly arrangement for labs running continuous research. We handle ongoing analysis needs, pipeline updates, troubleshooting, and support for grant reports — so your team is never blocked.",
             "price":"Inquire for terms","badge":"by_inquiry"},
        ],
        "price_label": "Transparent pricing", "price_title": "What each service includes",
        "price_sub": "Fixed-scope means no surprise invoices. Here is exactly what you get with each engagement.",
        "pricing": [
            {"service":"Genomic Analysis Pipelines","price":"From $2,000","timeline":"2–4 weeks",
             "includes":["Reproducible Nextflow / nf-core pipeline built for your data","Full QC report (FastQC / MultiQC)","Aligned and annotated output files","Plain-language results summary","1 round of revision included"]},
            {"service":"Variant Calling & Resistance Reporting","price":"From $1,200","timeline":"2–3 weeks",
             "includes":["GATK-based variant calling on your BAM/FASTQ files","Annotated variant table (VEP / ANNOVAR)","Resistance interpretation against known mutation databases","PDF-formatted report ready for clinical or research use","Follow-up Q&A call included"]},
            {"service":"AI-Powered Genomic Prediction","price":"Custom","timeline":"4–8 weeks",
             "includes":["Scoped model design based on your research question","Model training, validation, and performance report","Interpretable output (feature importance, confidence scores)","Full methodology documentation","Code and model delivered to you"]},
            {"service":"Training & Capacity Building","price":"From $300 / participant","timeline":"1–3 days",
             "includes":["Customised curriculum for your team's starting point","Hands-on practical sessions (not just slides)","All training materials and code notebooks provided","Post-workshop support channel (2 weeks)","Certificate of completion"]},
            {"service":"Drug Target & Repurposing Analysis","price":"Custom","timeline":"4–8 weeks",
             "includes":["AlphaFold structure retrieval or ColabFold prediction","Binding pocket analysis","Molecular docking screen against approved drug library","Ranked candidate shortlist with docking scores","Full methodology report"]},
        ],
        "tools_label": "Technology", "tools_title": "Tools & Stack",
        "tools_sub": "Industry-standard, reproducible, open-source tools — no black boxes.",
        "tools": [
            ("⚙️  Pipelines & Workflow", "Nextflow · nf-core · Snakemake · Docker / Singularity"),
            ("🧬  Analysis & Variant Calling", "GATK · samtools · BWA-MEM2 · STAR · bcftools · VEP / ANNOVAR"),
            ("🤖  ML & Data Science", "Python (scikit-learn, PyTorch) · R / Bioconductor · Graph neural networks · Neo4j"),
            ("🔬  Structural Bioinformatics", "AlphaFold DB · ColabFold · AutoDock Vina · DiffDock · py3Dmol"),
            ("☁️  Infrastructure", "AWS / GCP cloud compute · Large-scale genomic data storage · HPC compatible"),
            ("📊  Reporting", "MultiQC · Custom Streamlit dashboards · PDF clinical variant reports"),
        ],
        "about_label": "About", "about_title": "About Afrogenomics",
        "about_text": """Afrogenomics was founded to close a specific gap: African research institutions generate
            growing volumes of genomic and sequencing data, but the bioinformatics capacity to analyse it
            locally remains scarce — meaning analysis is routinely outsourced overseas, adding cost, delay,
            and distance from the people the research is meant to serve.<br/><br/>
            We work with universities, research institutes, NGOs, and diagnostics labs across Zimbabwe and
            the wider region to build pipelines, run analyses, and train local teams — so that capacity
            stays where the data and the need both are.<br/><br/>
            Our work spans HIV/TB genomic surveillance, agricultural genomics, drug-repurposing target
            discovery for neglected tropical diseases, and pipeline infrastructure for labs scaling up
            their omics capabilities.""",
        "creds_title": "Credentials",
        "creds": [
            "MSc Bioinformatics, University of Tübingen",
            "BSc Information Systems, Catholic University of Zimbabwe",
            "Azure Data Scientist Associate",
            "AWS Solutions Architect Associate",
            "Based in Harare, Zimbabwe",
        ],
        "founder_label": "Leadership", "founder_title": "About the Founder",
        "founder_role": "Founder, Afrogenomics",
        "founder_bio": """Farai is an AI/ML Engineer and Data Scientist with an MSc in Bioinformatics from the
            University of Tübingen and a Bachelor's degree in Information Systems from the Catholic University
            of Zimbabwe. He holds Azure Data Scientist Associate and AWS Solutions Architect Associate
            certifications.<br/><br/>His work spans fraud detection in finance, AI automation pipelines, and
            health-tech ventures — including graph neural network-based drug repurposing research for neglected
            tropical diseases and dermatology AI optimised for African skin tones.""",
        "faq_label": "Questions", "faq_title": "Frequently asked questions",
        "faqs": [
            ("Do I need to send you my raw sequencing files?",
             "Not necessarily. We can work with raw reads (FASTQ), aligned files (BAM), or variant files (VCF). If you have already processed your data partway, we pick up from wherever you are."),
            ("Is my data secure?",
             "Yes. All data is transferred over encrypted channels and stored securely on cloud infrastructure with access restricted to this engagement only. We do not share or retain your data after project completion."),
            ("Do I need my own sequencing machine?",
             "No. We handle only the computational analysis. If you need sequencing done, we can refer you to regional providers such as Inqaba Biotech in South Africa."),
            ("How long does a typical project take?",
             "Most pipeline and variant calling projects complete within 2–4 weeks. More complex ML or drug-repurposing projects typically take 4–8 weeks. We agree a specific timeline during scoping and stick to it."),
            ("Can you work with data from any sequencing platform?",
             "Yes — Illumina short reads, Oxford Nanopore long reads, Sanger sequencing, and most standard formats. Ask and we will confirm before any commitment."),
            ("What if I am not sure which service I need?",
             "That is fine — most clients are unsure at first. Just describe your research question and the data you have, and we will recommend the right approach."),
        ],
        "contact_label": "Get in touch", "contact_title": "Start a conversation",
        "contact_sub": "Tell us about your data and research question — we will respond within 24 hours.",
        "form_name": "Name", "form_email": "Email", "form_org": "Organisation",
        "form_service": "Service of interest", "form_message": "Tell us about your project",
        "form_submit": "Send inquiry →",
        "form_success": "Thank you — your inquiry has been sent. We will be in touch within 24 hours.",
        "form_fallback": "Message could not be sent automatically. Please email faraimupfuti@gmail.com or chat on WhatsApp.",
        "form_error": "Please fill in your name, email, and a short project description.",
        "direct_title": "Prefer to talk directly?",
        "direct_sub": "Most clients find it easier to explain their research question in a quick call or message.",
        "wa_btn": "💬 Chat on WhatsApp",
        "nav": {"services":"Services","tools":"Tools","about":"About","faq":"FAQ","contact":"Contact"},
    },

    "FR": {
        "flag": "🇫🇷", "label": "FR",
        "eyebrow": "🧬 Conseil en Bioinformatique · Harare, Zimbabwe",
        "hero_title": "Transformer les données de séquençage brutes en réponses pour la recherche africaine.",
        "hero_sub": "Nous construisons les pipelines d'analyse, l'infrastructure et l'interprétation dont les institutions de recherche africaines, les universités et les laboratoires de diagnostic ont besoin — sans les coûts ni les délais liés à l'externalisation outre-mer.",
        "hero_cta": "Consultation gratuite →",
        "hero_ghost": "Voir les services",
        "stat1_num": "10+", "stat1_label": "Projets pipeline & ML livrés",
        "stat2_num": "MSc", "stat2_label": "Bioinformatique, Université de Tübingen",
        "stat3_num": "2–4 sem.", "stat3_label": "Délai typique pour un projet pipeline",
        "stat4_num": "Local", "stat4_label": "Analyse locale, pas d'externalisation en Europe",
        "how_label": "Processus", "how_title": "Comment ça fonctionne",
        "how_sub": "Trois étapes du premier contact aux résultats entre vos mains.",
        "steps": [
            ("01", "Dites-nous ce que vous avez et ce dont vous avez besoin",
             "Partagez vos données de séquençage ou une description, votre question de recherche et votre délai. Aucun jargon technique requis — nous posons les bonnes questions pour cadrer le travail."),
            ("02", "Nous convenons d'un livrable fixe avant le début des travaux",
             "Vous recevez un cahier des charges court : exactement ce que nous analyserons, ce que vous recevrez, le calendrier et le coût. Aucune surprise. Vous ne procédez que lorsque vous êtes satisfait."),
            ("03", "Recevez vos résultats, clairement expliqués",
             "Nous livrons votre rapport avec un résumé en langage clair de ce que les résultats signifient pour votre recherche. Questions de suivi incluses sans frais supplémentaires."),
        ],
        "serve_label": "Qui nous aidons", "serve_title": "Qui nous servons",
        "serve_sub": "Nous travaillons avec toute organisation qui génère des données biologiques et a besoin d'une analyse experte.",
        "clients": [
            ("🏥", "Instituts de Recherche", "Programmes VIH, TB et MTN avec surveillance génomique active — comme BRTI et les groupes affiliés à KEMRI."),
            ("🎓", "Universités & Académie", "Groupes de recherche qui génèrent des données de séquençage mais manquent de personnel bioinformatique ou d'infrastructure de calcul."),
            ("🌍", "ONG & Santé Mondiale", "Programmes financés par PEPFAR, projets Wellcome Trust et initiatives Gates nécessitant une capacité bioinformatique africaine locale."),
            ("🧪", "Laboratoires de Diagnostic", "Laboratoires développant des services de tests génomiques qui ont besoin d'infrastructure pipeline sans équipe interne complète."),
            ("🌱", "Recherche Agricole", "Génomique des cultures et profilage de résistance aux maladies pour les exploitations commerciales et les organismes de recherche agricole."),
            ("💊", "Pharma & Biotech", "Entreprises ayant besoin d'analyses génomiques de populations africaines, de travail sur les cibles médicamenteuses pour MTN, ou de support bioinformatique."),
        ],
        "svc_label": "Ce que nous offrons", "svc_title": "Services",
        "svc_sub": "Chaque engagement a une portée fixe avec un livrable clair — vous savez exactement ce que vous obtenez avant le début des travaux.",
        "services": [
            {"icon":"🔬","title":"Pipelines d'Analyse Génomique","who":"Pour les laboratoires avec des données de séquençage non analysées",
             "desc":"Vous nous envoyez vos fichiers bruts. Nous construisons un flux de travail automatisé et reproductible, traitons vos données et retournons des résultats propres et annotés — prêts pour un article ou un rapport.",
             "price":"À partir de 2 000 $ / projet","badge":None},
            {"icon":"🧬","title":"Appel de Variants & Rapport de Résistance","who":"Pour les groupes de recherche sur le VIH, la TB et les maladies infectieuses",
             "desc":"Nous prenons votre sortie de séquençage brute et retournons un rapport formaté identifiant chaque mutation et signalant celles ayant des implications de résistance aux médicaments connues.",
             "price":"À partir de 1 200 $ / cohorte","badge":None},
            {"icon":"🤖","title":"Prédiction Génomique par IA","who":"Pour les chercheurs qui ont besoin de plus qu'une analyse standard",
             "desc":"Lorsque votre question va au-delà de l'identification des mutations — prédiction de réponse au traitement, identification de médicaments potentiels — nous construisons un modèle IA personnalisé sur vos données.",
             "price":"Devis sur mesure","badge":None},
            {"icon":"🎓","title":"Formation & Renforcement des Capacités","who":"Pour les universités, instituts et équipes de laboratoire",
             "desc":"Votre équipe collecte les données — nous leur apprenons à les analyser. Ateliers pratiques sur l'analyse de données génomiques, dispensés sur place à Harare ou à distance.",
             "price":"À partir de 300 $ / participant","badge":None},
            {"icon":"💊","title":"Analyse de Cibles Médicamenteuses","who":"Pour les programmes MTN, VIH et TB",
             "desc":"Nous identifions computationnellement quels médicaments approuvés existants ont un potentiel contre votre cible, en utilisant des structures protéiques prédites par IA et le criblage moléculaire.",
             "price":"Devis sur mesure","badge":None},
            {"icon":"🦠","title":"Analyse du Microbiome","who":"Pour les groupes de recherche clinique et environnementale",
             "desc":"Nous analysons vos données de séquençage et retournons un rapport complet avec composition des espèces, métriques de diversité et comparaisons entre groupes.",
             "price":"À partir de 1 800 $ / projet","badge":"coming_soon"},
            {"icon":"🔄","title":"Support de Recherche Continu","who":"Pour les laboratoires actifs ayant besoin d'un bioinformaticien disponible",
             "desc":"Un arrangement mensuel dédié pour les laboratoires menant des recherches continues. Nous gérons vos besoins d'analyse courants, mises à jour de pipelines et support pour les rapports de subventions.",
             "price":"Nous contacter","badge":"by_inquiry"},
        ],
        "price_label": "Tarification transparente", "price_title": "Ce qu'inclut chaque service",
        "price_sub": "Portée fixe signifie aucune facture surprise. Voici exactement ce que vous obtenez avec chaque engagement.",
        "pricing": [
            {"service":"Pipelines d'Analyse Génomique","price":"À partir de 2 000 $","timeline":"2–4 semaines",
             "includes":["Pipeline Nextflow / nf-core reproductible construit pour vos données","Rapport QC complet","Fichiers de sortie alignés et annotés","Résumé des résultats en langage clair","1 cycle de révision inclus"]},
            {"service":"Appel de Variants & Rapport de Résistance","price":"À partir de 1 200 $","timeline":"2–3 semaines",
             "includes":["Appel de variants basé sur GATK","Table de variants annotée","Interprétation de résistance","Rapport PDF prêt à l'emploi","Appel de suivi Q&A inclus"]},
            {"service":"Prédiction Génomique par IA","price":"Devis","timeline":"4–8 semaines",
             "includes":["Conception du modèle basée sur votre question","Formation, validation et rapport de performance","Sortie interprétable","Documentation complète","Code et modèle livrés"]},
            {"service":"Formation & Renforcement des Capacités","price":"À partir de 300 $ / participant","timeline":"1–3 jours",
             "includes":["Programme personnalisé","Sessions pratiques","Tous les matériaux fournis","Canal de support post-atelier (2 semaines)","Certificat de complétion"]},
            {"service":"Analyse de Cibles Médicamenteuses","price":"Devis","timeline":"4–8 semaines",
             "includes":["Récupération de structure AlphaFold","Analyse des sites de liaison","Criblage de docking moléculaire","Liste de candidats classée","Rapport de méthodologie complet"]},
        ],
        "tools_label": "Technologie", "tools_title": "Outils & Stack",
        "tools_sub": "Outils standard de l'industrie, reproductibles et open-source — aucune boîte noire.",
        "tools": [
            ("⚙️  Pipelines & Flux de travail", "Nextflow · nf-core · Snakemake · Docker / Singularity"),
            ("🧬  Analyse & Appel de Variants", "GATK · samtools · BWA-MEM2 · STAR · bcftools · VEP / ANNOVAR"),
            ("🤖  ML & Science des Données", "Python (scikit-learn, PyTorch) · R / Bioconductor · Réseaux de neurones graphiques"),
            ("🔬  Bioinformatique Structurale", "AlphaFold DB · ColabFold · AutoDock Vina · DiffDock · py3Dmol"),
            ("☁️  Infrastructure", "AWS / GCP · Stockage cloud pour données génomiques · Compatible HPC"),
            ("📊  Rapports", "MultiQC · Tableaux de bord Streamlit · Rapports PDF de variants cliniques"),
        ],
        "about_label": "À propos", "about_title": "À propos d'Afrogenomics",
        "about_text": """Afrogenomics a été fondée pour combler un écart spécifique : les institutions de recherche
            africaines génèrent des volumes croissants de données génomiques et de séquençage, mais la capacité
            bioinformatique pour les analyser localement reste rare — ce qui signifie que l'analyse est
            régulièrement externalisée à l'étranger, ajoutant des coûts, des délais et de la distance par rapport
            aux personnes que la recherche est censée servir.<br/><br/>Nous travaillons avec des universités,
            des instituts de recherche, des ONG et des laboratoires de diagnostic à travers le Zimbabwe et la
            région élargie pour construire des pipelines, exécuter des analyses et former des équipes locales.""",
        "creds_title": "Diplômes & Certifications",
        "creds": [
            "MSc Bioinformatique, Université de Tübingen",
            "BSc Systèmes d'Information, Université Catholique du Zimbabwe",
            "Azure Data Scientist Associate",
            "AWS Solutions Architect Associate",
            "Basé à Harare, Zimbabwe",
        ],
        "founder_label": "Direction", "founder_title": "À propos du Fondateur",
        "founder_role": "Fondateur, Afrogenomics",
        "founder_bio": """Farai est un Ingénieur IA/ML et Data Scientist avec un MSc en Bioinformatique de l'Université
            de Tübingen. Son travail couvre la détection de fraude en finance, les pipelines d'automatisation IA
            et les ventures de santé-tech — notamment la recherche de repositionnement de médicaments basée sur
            les réseaux de neurones graphiques pour les maladies tropicales négligées.""",
        "faq_label": "Questions", "faq_title": "Questions fréquemment posées",
        "faqs": [
            ("Dois-je vous envoyer mes fichiers de séquençage bruts ?",
             "Pas nécessairement. Nous pouvons travailler avec des lectures brutes (FASTQ), des fichiers alignés (BAM) ou des fichiers de variants (VCF). Nous vous dirons exactement quel format nous avons besoin lors de la définition du périmètre."),
            ("Mes données sont-elles sécurisées ?",
             "Oui. Toutes les données sont transférées via des canaux chiffrés et stockées en toute sécurité sur une infrastructure cloud. Nous ne partageons pas vos données après la fin du projet."),
            ("Ai-je besoin de ma propre machine de séquençage ?",
             "Non. Nous gérons uniquement l'analyse computationnelle. Si vous avez besoin d'un séquençage, nous pouvons vous référer à des prestataires régionaux comme Inqaba Biotech."),
            ("Combien de temps dure un projet typique ?",
             "La plupart des projets de pipeline se terminent en 2 à 4 semaines. Les projets ML ou de repositionnement de médicaments prennent généralement 4 à 8 semaines."),
            ("Pouvez-vous travailler avec des données de n'importe quelle plateforme de séquençage ?",
             "Oui — Illumina, Oxford Nanopore, Sanger et la plupart des formats standard. Demandez et nous confirmerons avant tout engagement."),
            ("Et si je ne suis pas sûr du service dont j'ai besoin ?",
             "C'est tout à fait normal. Décrivez simplement votre question de recherche et les données que vous avez, et nous recommanderons la bonne approche."),
        ],
        "contact_label": "Nous contacter", "contact_title": "Démarrer une conversation",
        "contact_sub": "Parlez-nous de vos données et de votre question de recherche — nous répondrons sous 24 heures.",
        "form_name": "Nom", "form_email": "E-mail", "form_org": "Organisation",
        "form_service": "Service d'intérêt", "form_message": "Parlez-nous de votre projet",
        "form_submit": "Envoyer la demande →",
        "form_success": "Merci — votre demande a été envoyée. Nous vous répondrons dans les 24 heures.",
        "form_fallback": "Le message n'a pas pu être envoyé automatiquement. Veuillez envoyer un e-mail à faraimupfuti@gmail.com.",
        "form_error": "Veuillez remplir votre nom, votre e-mail et une brève description du projet.",
        "direct_title": "Préférez-vous parler directement ?",
        "direct_sub": "La plupart des clients trouvent plus facile d'expliquer leur question en un rapide appel ou message.",
        "wa_btn": "💬 Chat WhatsApp",
        "nav": {"services":"Services","tools":"Outils","about":"À propos","faq":"FAQ","contact":"Contact"},
    },

    "PT": {
        "flag": "🇵🇹", "label": "PT",
        "eyebrow": "🧬 Consultoria em Bioinformática · Harare, Zimbabwe",
        "hero_title": "Transformando dados brutos de sequenciamento em respostas para a pesquisa africana.",
        "hero_sub": "Construímos os pipelines de análise, infraestrutura e interpretação que instituições de pesquisa africanas, universidades e laboratórios de diagnóstico precisam — sem o custo ou atraso de terceirizar a análise para o exterior.",
        "hero_cta": "Agendar consulta gratuita →",
        "hero_ghost": "Ver serviços",
        "stat1_num": "10+", "stat1_label": "Projetos de pipeline e ML entregues",
        "stat2_num": "MSc", "stat2_label": "Bioinformática, Universidade de Tübingen",
        "stat3_num": "2–4 sem.", "stat3_label": "Prazo típico para um projeto de pipeline",
        "stat4_num": "Local", "stat4_label": "Análise local, sem terceirização para Europa",
        "how_label": "Processo", "how_title": "Como funciona",
        "how_sub": "Três etapas do primeiro contato aos resultados em suas mãos.",
        "steps": [
            ("01", "Diga-nos o que você tem e o que precisa",
             "Compartilhe seus dados de sequenciamento ou uma descrição, sua pergunta de pesquisa e seu prazo. Sem jargão técnico — fazemos as perguntas certas para definir o escopo do trabalho."),
            ("02", "Acordamos um produto final fixo antes de começar qualquer trabalho",
             "Você recebe um escopo curto por escrito: exatamente o que analisaremos, o que você receberá, o cronograma e o custo. Sem surpresas. Você prossegue apenas quando estiver satisfeito."),
            ("03", "Receba seus resultados, explicados claramente",
             "Entregamos seu relatório com um resumo em linguagem simples do que os resultados significam para sua pesquisa. Perguntas de acompanhamento incluídas sem custo adicional."),
        ],
        "serve_label": "Quem ajudamos", "serve_title": "A quem servimos",
        "serve_sub": "Trabalhamos com qualquer organização que gera dados biológicos e precisa de análise especializada.",
        "clients": [
            ("🏥", "Institutos de Pesquisa", "Programas de HIV, TB e DNTs com vigilância genómica ativa — como BRTI e grupos afiliados ao KEMRI."),
            ("🎓", "Universidades & Academia", "Grupos de pesquisa que geram dados de sequenciamento mas carecem de pessoal bioinformático ou infraestrutura de computação."),
            ("🌍", "ONGs & Saúde Global", "Programas financiados pelo PEPFAR, projetos Wellcome Trust e iniciativas Gates que precisam de capacidade bioinformática africana local."),
            ("🧪", "Laboratórios de Diagnóstico", "Laboratórios expandindo para oferecer serviços de testes genómicos que precisam de infraestrutura de pipeline."),
            ("🌱", "Pesquisa Agrícola", "Genómica de culturas e perfil de resistência a doenças para fazendas comerciais e organismos de pesquisa agrícola."),
            ("💊", "Farmacêutica & Biotech", "Empresas que precisam de análises genómicas de populações africanas ou suporte bioinformático para ensaios clínicos."),
        ],
        "svc_label": "O que oferecemos", "svc_title": "Serviços",
        "svc_sub": "Cada contrato tem escopo fixo com produto final claro — você sabe exatamente o que receberá antes de começar.",
        "services": [
            {"icon":"🔬","title":"Pipelines de Análise Genómica","who":"Para laboratórios com dados de sequenciamento não analisados",
             "desc":"Você nos envia seus arquivos brutos de sequenciamento. Construímos um fluxo de trabalho automatizado e reproduzível, processamos seus dados e retornamos resultados limpos e anotados — prontos para uso em um artigo ou relatório.",
             "price":"A partir de $2.000 / projeto","badge":None},
            {"icon":"🧬","title":"Chamada de Variantes & Relatório de Resistência","who":"Para grupos de pesquisa em HIV, TB e doenças infecciosas",
             "desc":"Pegamos sua saída de sequenciamento bruta e retornamos um relatório formatado identificando cada mutação e sinalizando aquelas com implicações conhecidas de resistência a medicamentos.",
             "price":"A partir de $1.200 / coorte","badge":None},
            {"icon":"🤖","title":"Predição Genómica por IA","who":"Para pesquisadores que precisam de mais do que uma análise padrão",
             "desc":"Quando sua pergunta vai além de identificar mutações — prever resposta ao tratamento, identificar quais medicamentos podem funcionar contra um novo patógeno — construímos um modelo de IA personalizado nos seus dados.",
             "price":"Sob consulta","badge":None},
            {"icon":"🎓","title":"Treinamento & Capacitação","who":"Para universidades, institutos e equipes de laboratório",
             "desc":"Sua equipe coleta os dados — nós ensinamos a analisá-los. Workshops práticos em análise de dados genómicos, ministrados presencialmente em Harare ou remotamente.",
             "price":"A partir de $300 / participante","badge":None},
            {"icon":"💊","title":"Análise de Alvos & Reposicionamento de Fármacos","who":"Para programas de DNT, HIV e TB",
             "desc":"Identificamos computacionalmente quais medicamentos aprovados existentes têm potencial contra seu alvo, usando estruturas proteicas previstas por IA e triagem molecular.",
             "price":"Sob consulta","badge":None},
            {"icon":"🦠","title":"Análise do Microbioma","who":"Para grupos de pesquisa clínica e ambiental",
             "desc":"Analisamos seus dados de sequenciamento e retornamos um relatório completo com composição de espécies, métricas de diversidade e comparações entre grupos.",
             "price":"A partir de $1.800 / projeto","badge":"coming_soon"},
            {"icon":"🔄","title":"Suporte de Pesquisa Contínuo","who":"Para laboratórios ativos que precisam de um bioinformata disponível",
             "desc":"Um contrato mensal dedicado para laboratórios que conduzem pesquisas contínuas. Gerenciamos suas necessidades de análise contínuas, atualizações de pipeline e suporte para relatórios de bolsas.",
             "price":"Consultar","badge":"by_inquiry"},
        ],
        "price_label": "Preços transparentes", "price_title": "O que cada serviço inclui",
        "price_sub": "Escopo fixo significa sem faturas surpresa. Aqui está exatamente o que você obtém com cada contrato.",
        "pricing": [
            {"service":"Pipelines de Análise Genómica","price":"A partir de $2.000","timeline":"2–4 semanas",
             "includes":["Pipeline Nextflow / nf-core reproduzível","Relatório QC completo","Arquivos de saída alinhados e anotados","Resumo dos resultados em linguagem simples","1 rodada de revisão incluída"]},
            {"service":"Chamada de Variantes & Relatório de Resistência","price":"A partir de $1.200","timeline":"2–3 semanas",
             "includes":["Chamada de variantes baseada em GATK","Tabela de variantes anotada","Interpretação de resistência","Relatório PDF pronto para uso","Chamada de acompanhamento incluída"]},
            {"service":"Predição Genómica por IA","price":"Sob consulta","timeline":"4–8 semanas",
             "includes":["Design do modelo baseado na sua pergunta","Treinamento, validação e relatório de desempenho","Saída interpretável","Documentação completa","Código e modelo entregues"]},
            {"service":"Treinamento & Capacitação","price":"A partir de $300 / participante","timeline":"1–3 dias",
             "includes":["Currículo personalizado","Sessões práticas","Todos os materiais fornecidos","Canal de suporte pós-workshop (2 semanas)","Certificado de conclusão"]},
            {"service":"Análise de Alvos & Reposicionamento","price":"Sob consulta","timeline":"4–8 semanas",
             "includes":["Recuperação de estrutura AlphaFold","Análise do sítio de ligação","Triagem de docking molecular","Lista de candidatos classificada","Relatório de metodologia completo"]},
        ],
        "tools_label": "Tecnologia", "tools_title": "Ferramentas & Stack",
        "tools_sub": "Ferramentas padrão da indústria, reproduzíveis e de código aberto — sem caixas pretas.",
        "tools": [
            ("⚙️  Pipelines & Fluxo de Trabalho", "Nextflow · nf-core · Snakemake · Docker / Singularity"),
            ("🧬  Análise & Chamada de Variantes", "GATK · samtools · BWA-MEM2 · STAR · bcftools · VEP / ANNOVAR"),
            ("🤖  ML & Ciência de Dados", "Python (scikit-learn, PyTorch) · R / Bioconductor · Redes neurais em grafos"),
            ("🔬  Bioinformática Estrutural", "AlphaFold DB · ColabFold · AutoDock Vina · DiffDock · py3Dmol"),
            ("☁️  Infraestrutura", "AWS / GCP · Armazenamento em nuvem para dados genómicos · Compatível com HPC"),
            ("📊  Relatórios", "MultiQC · Dashboards Streamlit · Relatórios PDF de variantes clínicas"),
        ],
        "about_label": "Sobre", "about_title": "Sobre a Afrogenomics",
        "about_text": """A Afrogenomics foi fundada para fechar uma lacuna específica: as instituições de pesquisa
            africanas geram volumes crescentes de dados genómicos e de sequenciamento, mas a capacidade
            bioinformática para analisá-los localmente permanece escassa — o que significa que a análise é
            rotineiramente terceirizada para o exterior, adicionando custo, atraso e distância das pessoas
            que a pesquisa pretende servir.<br/><br/>Trabalhamos com universidades, institutos de pesquisa,
            ONGs e laboratórios de diagnóstico em todo o Zimbabwe e na região mais ampla para construir
            pipelines, executar análises e treinar equipes locais.""",
        "creds_title": "Credenciais",
        "creds": [
            "MSc Bioinformática, Universidade de Tübingen",
            "BSc Sistemas de Informação, Universidade Católica do Zimbabwe",
            "Azure Data Scientist Associate",
            "AWS Solutions Architect Associate",
            "Sediado em Harare, Zimbabwe",
        ],
        "founder_label": "Liderança", "founder_title": "Sobre o Fundador",
        "founder_role": "Fundador, Afrogenomics",
        "founder_bio": """Farai é um Engenheiro de IA/ML e Cientista de Dados com MSc em Bioinformática pela
            Universidade de Tübingen. Seu trabalho abrange deteção de fraude em finanças, pipelines de
            automação de IA e empreendimentos de saúde-tech — incluindo pesquisa de reposicionamento de
            fármacos baseada em redes neurais de grafos para doenças tropicais negligenciadas.""",
        "faq_label": "Perguntas", "faq_title": "Perguntas frequentes",
        "faqs": [
            ("Preciso enviar meus arquivos brutos de sequenciamento?",
             "Não necessariamente. Podemos trabalhar com leituras brutas (FASTQ), arquivos alinhados (BAM) ou arquivos de variantes (VCF). Diremos exatamente qual formato precisamos durante o escopo."),
            ("Meus dados são seguros?",
             "Sim. Todos os dados são transferidos por canais criptografados e armazenados com segurança em infraestrutura de nuvem. Não compartilhamos ou retemos seus dados após a conclusão do projeto."),
            ("Preciso de minha própria máquina de sequenciamento?",
             "Não. Lidamos apenas com a análise computacional. Se precisar de sequenciamento, podemos encaminhá-lo a fornecedores regionais como a Inqaba Biotech."),
            ("Quanto tempo dura um projeto típico?",
             "A maioria dos projetos de pipeline conclui em 2 a 4 semanas. Projetos mais complexos de ML ou reposicionamento de fármacos normalmente levam 4 a 8 semanas."),
            ("Vocês podem trabalhar com dados de qualquer plataforma de sequenciamento?",
             "Sim — Illumina, Oxford Nanopore, Sanger e a maioria dos formatos padrão. Pergunte e confirmaremos antes de qualquer compromisso."),
            ("E se eu não tiver certeza de qual serviço preciso?",
             "Tudo bem — a maioria dos clientes não tem certeza no primeiro contato. Descreva sua pergunta de pesquisa e os dados que você tem, e recomendaremos a abordagem certa."),
        ],
        "contact_label": "Entre em contato", "contact_title": "Iniciar uma conversa",
        "contact_sub": "Fale-nos sobre seus dados e sua pergunta de pesquisa — responderemos em 24 horas.",
        "form_name": "Nome", "form_email": "E-mail", "form_org": "Organização",
        "form_service": "Serviço de interesse", "form_message": "Fale-nos sobre seu projeto",
        "form_submit": "Enviar consulta →",
        "form_success": "Obrigado — sua consulta foi enviada. Entraremos em contato em 24 horas.",
        "form_fallback": "A mensagem não pôde ser enviada automaticamente. Por favor, envie um e-mail para faraimupfuti@gmail.com.",
        "form_error": "Por favor, preencha seu nome, e-mail e uma breve descrição do projeto.",
        "direct_title": "Prefere falar diretamente?",
        "direct_sub": "A maioria dos clientes acha mais fácil explicar sua pergunta de pesquisa em uma chamada rápida.",
        "wa_btn": "💬 Chat WhatsApp",
        "nav": {"services":"Serviços","tools":"Ferramentas","about":"Sobre","faq":"FAQ","contact":"Contato"},
    },
}

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Afrogenomics | Bioinformatics Consultancy",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── SESSION STATE ────────────────────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "EN"
L = LANG[st.session_state.lang]

# ─── DESIGN SYSTEM ────────────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body,.stApp,[data-testid="stAppViewContainer"],section.main,.block-container{background-color:#071612!important;font-family:'Inter',sans-serif!important;color:#C8C4B6!important;}
#MainMenu,footer,header{visibility:hidden;}
[data-testid="stToolbar"]{display:none;}
.block-container{padding:0 2.5rem 4rem!important;max-width:1200px!important;}
h1,h2,h3,h4{font-family:'Playfair Display',Georgia,serif!important;color:#F0EDE4!important;line-height:1.25;}
h1{font-size:3rem!important;font-weight:700!important;letter-spacing:-0.5px;}
h2{font-size:2rem!important;font-weight:600!important;margin-bottom:0.4rem;}
h3{font-size:1.15rem!important;font-weight:600!important;}
p,li,span{color:#C8C4B6!important;font-family:'Inter',sans-serif!important;line-height:1.7;}
.ag-nav{display:flex;align-items:center;justify-content:space-between;padding:1.1rem 0 1rem;border-bottom:1px solid #1A3830;margin-bottom:0;}
.ag-logo{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;color:#F0EDE4!important;letter-spacing:-0.3px;}
.ag-logo span{color:#4CAF82;}
.ag-nav-right{display:flex;align-items:center;gap:2rem;}
.ag-nav-links{display:flex;gap:2rem;}
.ag-nav-links a{color:#9A9688!important;text-decoration:none;font-size:0.875rem;font-weight:500;letter-spacing:0.02em;transition:color 0.2s;}
.ag-nav-links a:hover{color:#4CAF82!important;}
.lang-btn{background:transparent;border:1px solid #1A3830;color:#9A9688!important;font-size:0.75rem;font-weight:600;padding:0.3rem 0.6rem;border-radius:4px;cursor:pointer;font-family:'Inter',sans-serif;transition:all 0.2s;}
.lang-btn:hover,.lang-btn.active{border-color:#4CAF82;color:#4CAF82!important;background:rgba(76,175,130,0.06);}
.ag-hero{padding:5rem 0 4rem;position:relative;overflow:hidden;}
.ag-hero::before{content:'';position:absolute;top:-80px;right:-120px;width:500px;height:500px;background:radial-gradient(circle,rgba(76,175,130,0.07) 0%,transparent 70%);pointer-events:none;}
.ag-hero::after{content:'';position:absolute;bottom:-60px;left:-80px;width:350px;height:350px;background:radial-gradient(circle,rgba(76,175,130,0.05) 0%,transparent 70%);pointer-events:none;}
.ag-eyebrow{display:inline-block;font-family:'Inter',sans-serif;font-size:0.72rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#4CAF82!important;border:1px solid rgba(76,175,130,0.3);border-radius:100px;padding:0.3rem 0.9rem;margin-bottom:1.5rem;}
.ag-hero-title{font-family:'Playfair Display',serif!important;font-size:3.2rem!important;font-weight:700!important;color:#F0EDE4!important;line-height:1.18!important;max-width:780px;margin-bottom:1.2rem;}
.ag-hero-sub{font-size:1.05rem;color:#9A9688!important;max-width:580px;line-height:1.75;margin-bottom:2rem;}
.ag-btn-primary{display:inline-block;background:linear-gradient(135deg,#4CAF82 0%,#2E8B5A 100%);color:#071612!important;font-family:'Inter',sans-serif;font-weight:700;font-size:0.9rem;padding:0.8rem 1.8rem;border-radius:6px;text-decoration:none;letter-spacing:0.01em;box-shadow:0 4px 24px rgba(76,175,130,0.25);transition:all 0.2s;}
.ag-btn-primary:hover{box-shadow:0 6px 32px rgba(76,175,130,0.4);transform:translateY(-1px);color:#071612!important;}
.ag-btn-ghost{display:inline-block;background:transparent;color:#C8C4B6!important;font-family:'Inter',sans-serif;font-weight:600;font-size:0.9rem;padding:0.8rem 1.8rem;border-radius:6px;border:1px solid #2A4A3F;text-decoration:none;margin-left:0.75rem;transition:all 0.2s;}
.ag-btn-ghost:hover{border-color:#4CAF82;color:#4CAF82!important;}
.ag-stats{display:flex;gap:0;border:1px solid #1A3830;border-radius:10px;background:#0D2218;overflow:hidden;margin:0;}
.ag-stat{flex:1;padding:1.6rem 1.4rem;border-right:1px solid #1A3830;text-align:center;}
.ag-stat:last-child{border-right:none;}
.ag-stat-num{font-family:'Playfair Display',serif;font-size:2rem;font-weight:700;color:#4CAF82!important;display:block;margin-bottom:0.3rem;}
.ag-stat-label{font-size:0.8rem;color:#6B6860!important;line-height:1.4;}
.ag-section{padding:4.5rem 0 1rem;}
.ag-section-label{font-size:0.72rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#4CAF82!important;margin-bottom:0.5rem;display:block;}
.ag-section-title{font-family:'Playfair Display',serif;font-size:2rem;color:#F0EDE4!important;margin-bottom:0.5rem;}
.ag-section-sub{color:#7A7870!important;font-size:0.95rem;margin-bottom:2rem;max-width:600px;}
.ag-divider{border:none;border-top:1px solid #1A3830;margin:3rem 0;}
.ag-step{background:#0D2218;border:1px solid #1A3830;border-radius:10px;padding:2rem;height:100%;transition:border-color 0.2s;}
.ag-step:hover{border-color:#2E6B4F;}
.ag-step-num{font-family:'Playfair Display',serif;font-size:3rem;font-weight:700;color:rgba(76,175,130,0.15)!important;line-height:1;margin-bottom:1rem;}
.ag-step h3{font-size:1rem!important;margin-bottom:0.75rem;color:#F0EDE4!important;}
.ag-step p{font-size:0.875rem;color:#7A7870!important;line-height:1.7;}
.ag-client-card{background:#0D2218;border:1px solid #1A3830;border-radius:10px;padding:1.6rem;margin-bottom:1rem;transition:border-color 0.2s,transform 0.2s;}
.ag-client-card:hover{border-color:#2E6B4F;transform:translateY(-2px);}
.ag-client-icon{font-size:1.8rem;margin-bottom:0.8rem;display:block;}
.ag-client-card h3{font-size:0.95rem!important;color:#F0EDE4!important;margin-bottom:0.5rem;}
.ag-client-card p{font-size:0.83rem;color:#7A7870!important;line-height:1.65;}
.ag-service-card{background:#0D2218;border:1px solid #1A3830;border-radius:10px;padding:1.75rem;height:100%;margin-bottom:1rem;transition:border-color 0.25s,transform 0.2s,box-shadow 0.2s;position:relative;overflow:hidden;}
.ag-service-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#4CAF82,#2E8B5A);opacity:0;transition:opacity 0.25s;}
.ag-service-card:hover{border-color:#2E6B4F;transform:translateY(-2px);box-shadow:0 8px 32px rgba(0,0,0,0.3);}
.ag-service-card:hover::before{opacity:1;}
.ag-card-icon{font-size:1.6rem;margin-bottom:0.8rem;display:block;}
.ag-card-badge{display:inline-block;font-size:0.68rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;padding:0.25rem 0.6rem;border-radius:4px;margin-bottom:0.6rem;}
.ag-badge-soon{background:rgba(217,164,65,0.12);color:#D9A441!important;border:1px solid rgba(217,164,65,0.3);}
.ag-badge-inquiry{background:rgba(76,175,130,0.08);color:#4CAF82!important;border:1px solid rgba(76,175,130,0.25);}
.ag-card-title{font-size:1.05rem!important;margin-bottom:0.3rem;color:#F0EDE4!important;}
.ag-card-who{font-size:0.78rem;color:#4CAF82!important;font-style:italic;margin-bottom:0.75rem;}
.ag-card-desc{font-size:0.855rem;color:#7A7870!important;line-height:1.7;margin-bottom:1rem;}
.ag-card-price{font-size:0.9rem;font-weight:700;color:#4CAF82!important;}
.ag-price-card{background:#0D2218;border:1px solid #1A3830;border-radius:10px;padding:1.75rem;margin-bottom:1rem;transition:border-color 0.2s;}
.ag-price-card:hover{border-color:#2E6B4F;}
.ag-price-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1rem;padding-bottom:1rem;border-bottom:1px solid #1A3830;}
.ag-price-name{font-size:1rem;font-weight:600;color:#F0EDE4!important;}
.ag-price-right{text-align:right;}
.ag-price-amount{font-size:1.1rem;font-weight:700;color:#4CAF82!important;display:block;}
.ag-price-timeline{font-size:0.78rem;color:#6B6860!important;}
.ag-price-includes{list-style:none;padding:0;margin:0;}
.ag-price-includes li{font-size:0.845rem;color:#7A7870!important;padding:0.3rem 0;display:flex;align-items:flex-start;gap:0.5rem;line-height:1.5;}
.ag-price-includes li::before{content:'✓';color:#4CAF82;font-weight:700;flex-shrink:0;margin-top:0.05rem;}
.ag-tool-card{background:#0D2218;border:1px solid #1A3830;border-radius:10px;padding:1.4rem 1.6rem;margin-bottom:1rem;}
.ag-tool-card h3{font-size:0.9rem!important;color:#F0EDE4!important;margin-bottom:0.5rem;}
.ag-tool-card p{font-size:0.82rem;color:#6B6860!important;line-height:1.65;}
.ag-about-text{font-size:0.95rem;color:#9A9688!important;line-height:1.85;}
.ag-cred-card{background:#0D2218;border:1px solid #1A3830;border-radius:10px;padding:1.6rem;}
.ag-cred-card h3{font-size:1rem!important;margin-bottom:1rem;}
.ag-cred-item{display:flex;align-items:flex-start;gap:0.6rem;margin-bottom:0.7rem;font-size:0.85rem;color:#9A9688!important;}
.ag-cred-dot{color:#4CAF82!important;font-size:0.7rem;margin-top:0.35rem;flex-shrink:0;}
.ag-founder-name{font-family:'Playfair Display',serif;font-size:1.5rem;color:#F0EDE4!important;margin-bottom:0.2rem;}
.ag-founder-role{font-size:0.85rem;color:#4CAF82!important;margin-bottom:1.2rem;font-style:italic;}
.ag-founder-bio{font-size:0.9rem;color:#9A9688!important;line-height:1.8;margin-bottom:1.4rem;}
.ag-contact-link{display:block;font-size:0.88rem;color:#9A9688!important;margin-bottom:0.5rem;text-decoration:none;}
.ag-contact-link:hover{color:#4CAF82!important;}
.stExpander{background:#0D2218!important;border:1px solid #1A3830!important;border-radius:8px!important;margin-bottom:0.6rem!important;}
.stExpander summary{color:#C8C4B6!important;font-size:0.92rem!important;font-weight:500!important;}
.ag-contact-card{background:#0D2218;border:1px solid #1A3830;border-radius:10px;padding:2rem;height:100%;}
.ag-contact-card h3{font-size:1.1rem!important;margin-bottom:0.5rem;}
.ag-contact-card p{font-size:0.875rem;color:#7A7870!important;margin-bottom:1.2rem;}
.ag-wa-btn{display:inline-block;background:#25D366;color:#fff!important;font-weight:700;font-size:0.875rem;padding:0.75rem 1.4rem;border-radius:6px;text-decoration:none;margin-top:0.5rem;}
.ag-direct-link{display:block;font-size:0.875rem;color:#9A9688!important;margin-bottom:0.6rem;text-decoration:none;}
.ag-direct-link:hover{color:#4CAF82!important;}
.stTextInput>div>div>input,.stTextArea>div>div>textarea,.stSelectbox>div>div>div{background-color:#0D2218!important;border:1px solid #1A3830!important;border-radius:6px!important;color:#C8C4B6!important;font-family:'Inter',sans-serif!important;font-size:0.875rem!important;}
.stTextInput>div>div>input:focus,.stTextArea>div>div>textarea:focus{border-color:#4CAF82!important;box-shadow:0 0 0 2px rgba(76,175,130,0.15)!important;}
label[data-testid="stWidgetLabel"] p{color:#9A9688!important;font-size:0.82rem!important;font-weight:500!important;margin-bottom:0.3rem;}
.stFormSubmitButton>button{background:linear-gradient(135deg,#4CAF82,#2E8B5A)!important;color:#071612!important;font-weight:700!important;font-size:0.9rem!important;border:none!important;border-radius:6px!important;padding:0.75rem 2rem!important;width:100%!important;box-shadow:0 4px 20px rgba(76,175,130,0.2)!important;}
.stFormSubmitButton>button:hover{box-shadow:0 6px 28px rgba(76,175,130,0.35)!important;}
.ag-footer{text-align:center;padding:2.5rem 0 1rem;border-top:1px solid #1A3830;font-size:0.8rem;color:#4A4840!important;}
</style>
""", unsafe_allow_html=True)

# ─── NAVBAR ───────────────────────────────────────────────────────────────────
nav_left, nav_right = st.columns([2, 3])
with nav_left:
    st.markdown('<div class="ag-logo">Afro<span>genomics</span></div>', unsafe_allow_html=True)
with nav_right:
    nr1, nr2, nr3, nr4 = st.columns([3, 1, 1, 1])
    with nr1:
        st.markdown(f"""
        <div class="ag-nav-links">
            <a href="#services">{L['nav']['services']}</a>
            <a href="#tools">{L['nav']['tools']}</a>
            <a href="#about">{L['nav']['about']}</a>
            <a href="#faq">{L['nav']['faq']}</a>
            <a href="#contact">{L['nav']['contact']}</a>
        </div>
        """, unsafe_allow_html=True)
    with nr2:
        if st.button("🇬🇧 EN", key="btn_en", use_container_width=True):
            st.session_state.lang = "EN"; st.rerun()
    with nr3:
        if st.button("🇫🇷 FR", key="btn_fr", use_container_width=True):
            st.session_state.lang = "FR"; st.rerun()
    with nr4:
        if st.button("🇵🇹 PT", key="btn_pt", use_container_width=True):
            st.session_state.lang = "PT"; st.rerun()

st.markdown('<hr class="ag-divider" style="margin:0 0 0 0;">', unsafe_allow_html=True)

# ─── HERO ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="ag-hero">
    <span class="ag-eyebrow">{L['eyebrow']}</span>
    <h1 class="ag-hero-title">{L['hero_title']}</h1>
    <p class="ag-hero-sub">{L['hero_sub']}</p>
    <a href="#contact" class="ag-btn-primary">{L['hero_cta']}</a>
    <a href="#services" class="ag-btn-ghost">{L['hero_ghost']}</a>
</div>
""", unsafe_allow_html=True)

# ─── STATS ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="ag-stats">
    <div class="ag-stat"><span class="ag-stat-num">{L['stat1_num']}</span><span class="ag-stat-label">{L['stat1_label']}</span></div>
    <div class="ag-stat"><span class="ag-stat-num">{L['stat2_num']}</span><span class="ag-stat-label">{L['stat2_label']}</span></div>
    <div class="ag-stat"><span class="ag-stat-num">{L['stat3_num']}</span><span class="ag-stat-label">{L['stat3_label']}</span></div>
    <div class="ag-stat"><span class="ag-stat-num">{L['stat4_num']}</span><span class="ag-stat-label">{L['stat4_label']}</span></div>
</div>
""", unsafe_allow_html=True)

# ─── HOW IT WORKS ─────────────────────────────────────────────────────────────
st.markdown(f"""<div class="ag-section">
    <span class="ag-section-label">{L['how_label']}</span>
    <h2 class="ag-section-title">{L['how_title']}</h2>
    <p class="ag-section-sub">{L['how_sub']}</p>
</div>""", unsafe_allow_html=True)
hw1, hw2, hw3 = st.columns(3)
for col, (num, title, desc) in zip([hw1, hw2, hw3], L["steps"]):
    with col:
        st.markdown(f'<div class="ag-step"><div class="ag-step-num">{num}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

st.markdown('<hr class="ag-divider">', unsafe_allow_html=True)

# ─── WHO WE SERVE ─────────────────────────────────────────────────────────────
st.markdown(f"""<div id="clients" class="ag-section" style="padding-top:1rem;">
    <span class="ag-section-label">{L['serve_label']}</span>
    <h2 class="ag-section-title">{L['serve_title']}</h2>
    <p class="ag-section-sub">{L['serve_sub']}</p>
</div>""", unsafe_allow_html=True)
cc = st.columns(3)
for i, (icon, title, desc) in enumerate(L["clients"]):
    with cc[i % 3]:
        st.markdown(f"""
        <div class="ag-client-card">
            <span class="ag-client-icon">{icon}</span>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>""", unsafe_allow_html=True)

st.markdown('<hr class="ag-divider">', unsafe_allow_html=True)

# ─── SERVICES ─────────────────────────────────────────────────────────────────
st.markdown(f"""<div id="services" class="ag-section" style="padding-top:1rem;">
    <span class="ag-section-label">{L['svc_label']}</span>
    <h2 class="ag-section-title">{L['svc_title']}</h2>
    <p class="ag-section-sub">{L['svc_sub']}</p>
</div>""", unsafe_allow_html=True)
sc = st.columns(3)
for i, svc in enumerate(L["services"]):
    with sc[i % 3]:
        badge_html = ""
        if svc["badge"] == "coming_soon":
            badge_html = f'<span class="ag-card-badge ag-badge-soon">Coming Soon</span><br/>'
        elif svc["badge"] == "by_inquiry":
            badge_html = f'<span class="ag-card-badge ag-badge-inquiry">By Inquiry</span><br/>'
        st.markdown(f"""
        <div class="ag-service-card">
            <span class="ag-card-icon">{svc['icon']}</span>
            {badge_html}
            <h3 class="ag-card-title">{svc['title']}</h3>
            <p class="ag-card-who">{svc['who']}</p>
            <p class="ag-card-desc">{svc['desc']}</p>
            <span class="ag-card-price">{svc['price']}</span>
        </div>""", unsafe_allow_html=True)

st.markdown('<hr class="ag-divider">', unsafe_allow_html=True)

# ─── PRICING ──────────────────────────────────────────────────────────────────
st.markdown(f"""<div id="pricing" class="ag-section" style="padding-top:1rem;">
    <span class="ag-section-label">{L['price_label']}</span>
    <h2 class="ag-section-title">{L['price_title']}</h2>
    <p class="ag-section-sub">{L['price_sub']}</p>
</div>""", unsafe_allow_html=True)
pc1, pc2 = st.columns(2)
for i, p in enumerate(L["pricing"]):
    with [pc1, pc2][i % 2]:
        items_html = "".join([f"<li>{item}</li>" for item in p["includes"]])
        st.markdown(f"""
        <div class="ag-price-card">
            <div class="ag-price-header">
                <span class="ag-price-name">{p['service']}</span>
                <div class="ag-price-right">
                    <span class="ag-price-amount">{p['price']}</span>
                    <span class="ag-price-timeline">⏱ {p['timeline']}</span>
                </div>
            </div>
            <ul class="ag-price-includes">{items_html}</ul>
        </div>""", unsafe_allow_html=True)

st.markdown('<hr class="ag-divider">', unsafe_allow_html=True)

# ─── TOOLS ────────────────────────────────────────────────────────────────────
st.markdown(f"""<div id="tools" class="ag-section" style="padding-top:1rem;">
    <span class="ag-section-label">{L['tools_label']}</span>
    <h2 class="ag-section-title">{L['tools_title']}</h2>
    <p class="ag-section-sub">{L['tools_sub']}</p>
</div>""", unsafe_allow_html=True)
tc1, tc2, tc3 = st.columns(3)
for i, (title, desc) in enumerate(L["tools"]):
    with [tc1, tc2, tc3][i % 3]:
        st.markdown(f'<div class="ag-tool-card"><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

st.markdown('<hr class="ag-divider">', unsafe_allow_html=True)

# ─── ABOUT ────────────────────────────────────────────────────────────────────
st.markdown(f"""<div id="about" class="ag-section" style="padding-top:1rem;">
    <span class="ag-section-label">{L['about_label']}</span>
    <h2 class="ag-section-title">{L['about_title']}</h2>
</div>""", unsafe_allow_html=True)
a1, a2 = st.columns([2, 1])
with a1:
    st.markdown(f'<p class="ag-about-text">{L["about_text"]}</p>', unsafe_allow_html=True)
with a2:
    creds_html = "".join([f'<div class="ag-cred-item"><span class="ag-cred-dot">▸</span><span>{c}</span></div>' for c in L["creds"]])
    st.markdown(f'<div class="ag-cred-card"><h3>{L["creds_title"]}</h3>{creds_html}</div>', unsafe_allow_html=True)

st.markdown('<hr class="ag-divider">', unsafe_allow_html=True)

# ─── FOUNDER ──────────────────────────────────────────────────────────────────
st.markdown(f"""<div class="ag-section" style="padding-top:1rem;">
    <span class="ag-section-label">{L['founder_label']}</span>
    <h2 class="ag-section-title">{L['founder_title']}</h2>
</div>""", unsafe_allow_html=True)
f1, f2 = st.columns([1, 2])
with f1:
    st.image("farai.jpg", use_container_width=True)
with f2:
    st.markdown(f"""
    <p class="ag-founder-name">Farai Mupfuti</p>
    <p class="ag-founder-role">{L['founder_role']}</p>
    <p class="ag-founder-bio">{L['founder_bio']}</p>
    <a class="ag-contact-link" href="tel:+263775643044">📞 +263 77 564 3044</a>
    <a class="ag-contact-link" href="mailto:faraimupfuti@gmail.com">📧 faraimupfuti@gmail.com</a>
    <a class="ag-contact-link" href="https://faraimupfuti.streamlit.app" target="_blank">🔗 Portfolio / Resume</a>
    """, unsafe_allow_html=True)

st.markdown('<hr class="ag-divider">', unsafe_allow_html=True)

# ─── FAQ ──────────────────────────────────────────────────────────────────────
st.markdown(f"""<div id="faq" class="ag-section" style="padding-top:1rem;">
    <span class="ag-section-label">{L['faq_label']}</span>
    <h2 class="ag-section-title">{L['faq_title']}</h2>
</div>""", unsafe_allow_html=True)
for q, a in L["faqs"]:
    with st.expander(q):
        st.markdown(f"<p>{a}</p>", unsafe_allow_html=True)

st.markdown('<hr class="ag-divider">', unsafe_allow_html=True)

# ─── CONTACT ──────────────────────────────────────────────────────────────────
st.markdown(f"""<div id="contact" class="ag-section" style="padding-top:1rem;">
    <span class="ag-section-label">{L['contact_label']}</span>
    <h2 class="ag-section-title">{L['contact_title']}</h2>
    <p class="ag-section-sub">{L['contact_sub']}</p>
</div>""", unsafe_allow_html=True)
ct1, ct2 = st.columns([2, 1])
with ct1:
    with st.form("contact_form"):
        fc1, fc2 = st.columns(2)
        with fc1:
            name  = st.text_input(L["form_name"])
            email = st.text_input(L["form_email"])
        with fc2:
            org     = st.text_input(L["form_org"])
            service = st.selectbox(L["form_service"], [s["title"] for s in L["services"]])
        message   = st.text_area(L["form_message"], height=130)
        submitted = st.form_submit_button(L["form_submit"])
        if submitted:
            if name and email and message:
                sent = send_inquiry_email(name, email, org, service, message)
                if sent:
                    st.success(L["form_success"])
                else:
                    st.warning(L["form_fallback"])
            else:
                st.error(L["form_error"])
with ct2:
    st.markdown(f"""
    <div class="ag-contact-card">
        <h3>{L['direct_title']}</h3>
        <p>{L['direct_sub']}</p>
        <a class="ag-direct-link" href="tel:+263775643044">📞 +263 77 564 3044</a>
        <a class="ag-direct-link" href="mailto:faraimupfuti@gmail.com">📧 faraimupfuti@gmail.com</a>
        <a class="ag-direct-link" href="https://faraimupfuti.streamlit.app" target="_blank">🔗 Portfolio / Resume</a>
        <br/>
        <a class="ag-wa-btn" href="https://wa.me/263775643044?text=Hi%20Farai%2C%20I%20found%20Afrogenomics%20and%20would%20like%20to%20discuss%20a%20project." target="_blank">
            {L['wa_btn']}
        </a>
    </div>""", unsafe_allow_html=True)

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ag-footer">
    <p>© 2025 Afrogenomics · Bioinformatics Consultancy · Harare, Zimbabwe</p>
    <p style="margin-top:0.4rem;">+263 77 564 3044 · faraimupfuti@gmail.com</p>
</div>
""", unsafe_allow_html=True)
