"""
Plant Disease Knowledge Base

This module contains structured educational information
associated with the 38 PlantVillage classes used by the
baseline CNN.

The CNN performs the visual classification.
This module only provides contextual information about
the predicted class.

Treatment information is intentionally general.
Specific chemical products, dosage, application timing,
and legal restrictions should be obtained from local
agricultural authorities and product labels.
"""


DISEASE_INFORMATION = {

    # ==========================================================
    # APPLE
    # ==========================================================

    "Apple___Apple_scab": {
        "plant": "Apple",
        "disease": "Apple Scab",
        "category": "Fungal disease",

        "description": (
            "Apple scab is a fungal disease that commonly affects "
            "apple leaves and fruit. It can produce olive-green to "
            "brown lesions and may lead to premature leaf loss."
        ),

        "symptoms": [
            "Olive-green or brown spots on leaves",
            "Darkening of older lesions",
            "Premature leaf drop",
            "Scabby or cork-like lesions may develop on fruit"
        ],

        "management": [
            "Remove and dispose of heavily affected fallen leaves "
            "and plant debris.",
            "Maintain good airflow around the tree through appropriate "
            "pruning and spacing.",
            "Avoid practices that unnecessarily keep foliage wet.",
            "Monitor new leaves regularly during periods favorable "
            "to disease development.",
            "If fungicide treatment is required, use only products "
            "approved for apple scab in your region and follow the label."
        ],

        "prevention": [
            "Maintain good orchard sanitation.",
            "Remove infected leaf debris.",
            "Maintain adequate airflow through the canopy.",
            "Monitor plants regularly during favorable weather."
        ]
    },


    "Apple___Black_rot": {
        "plant": "Apple",
        "disease": "Black Rot",
        "category": "Fungal disease",

        "description": (
            "Black rot is a fungal disease that can affect apple "
            "leaves, fruit, and woody tissues."
        ),

        "symptoms": [
            "Circular brown or purple leaf spots",
            "Darkening and enlargement of lesions",
            "Fruit decay that can become dark or black",
            "Dead or weakened woody tissue may occur"
        ],

        "management": [
            "Remove diseased fruit and infected plant material.",
            "Prune affected dead or diseased branches where appropriate.",
            "Improve canopy airflow.",
            "Remove mummified fruit from the tree and surrounding area.",
            "Use locally approved disease-management products when necessary."
        ],

        "prevention": [
            "Maintain orchard sanitation.",
            "Remove dead and diseased wood.",
            "Remove mummified fruit.",
            "Maintain good canopy airflow."
        ]
    },


    "Apple___Cedar_apple_rust": {
        "plant": "Apple",
        "disease": "Cedar Apple Rust",
        "category": "Fungal disease",

        "description": (
            "Cedar apple rust is a fungal disease involving apple and "
            "certain cedar or juniper hosts during its life cycle."
        ),

        "symptoms": [
            "Yellow to orange spots on apple leaves",
            "Orange or rust-colored structures on affected foliage",
            "Premature leaf loss in severe cases",
            "Fruit symptoms may occasionally develop"
        ],

        "management": [
            "Monitor apple trees during periods favorable to rust development.",
            "Remove severely affected plant material where practical.",
            "Manage nearby alternate hosts when appropriate and feasible.",
            "Use locally approved fungicide programs when necessary."
        ],

        "prevention": [
            "Monitor plants regularly.",
            "Maintain healthy tree growth.",
            "Reduce disease sources where practical.",
            "Follow locally recommended rust-management practices."
        ]
    },


    "Apple___healthy": {
        "plant": "Apple",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "apple leaf based on the visual patterns it learned."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal plant care.",
            "Monitor new growth regularly.",
            "Maintain appropriate watering, nutrition, and airflow."
        ],

        "prevention": [
            "Inspect leaves regularly.",
            "Maintain good sanitation.",
            "Provide appropriate growing conditions."
        ]
    },


    # ==========================================================
    # BLUEBERRY
    # ==========================================================

    "Blueberry___healthy": {
        "plant": "Blueberry",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "blueberry leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue routine plant care.",
            "Monitor foliage and fruit regularly.",
            "Maintain suitable growing conditions."
        ],

        "prevention": [
            "Maintain good sanitation.",
            "Monitor plants regularly.",
            "Avoid unnecessary plant stress."
        ]
    },


    # ==========================================================
    # CHERRY
    # ==========================================================

    "Cherry_(including_sour)___Powdery_mildew": {
        "plant": "Cherry",
        "disease": "Powdery Mildew",
        "category": "Fungal disease",

        "description": (
            "Powdery mildew is a fungal disease that produces a "
            "characteristic powdery growth on susceptible plant tissues."
        ),

        "symptoms": [
            "White or gray powdery growth",
            "Distorted young leaves",
            "Reduced leaf quality",
            "Affected shoots may show stunted growth"
        ],

        "management": [
            "Improve airflow around the plant.",
            "Remove severely affected plant material where appropriate.",
            "Avoid excessive conditions that encourage dense, humid foliage.",
            "Use locally approved powdery mildew treatments when necessary."
        ],

        "prevention": [
            "Maintain adequate spacing.",
            "Promote good airflow.",
            "Monitor young foliage.",
            "Avoid excessive plant density."
        ]
    },


    "Cherry_(including_sour)___healthy": {
        "plant": "Cherry",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "cherry leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal plant care.",
            "Monitor foliage regularly."
        ],

        "prevention": [
            "Maintain sanitation.",
            "Maintain appropriate airflow.",
            "Inspect plants regularly."
        ]
    },


    # ==========================================================
    # CORN
    # ==========================================================

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "plant": "Corn",
        "disease": "Cercospora Leaf Spot / Gray Leaf Spot",
        "category": "Fungal disease",

        "description": (
            "Gray leaf spot is a fungal disease of corn that can "
            "produce elongated lesions on leaves."
        ),

        "symptoms": [
            "Long rectangular or elongated gray-brown lesions",
            "Lesions may follow leaf veins",
            "Increasing numbers of lesions on older foliage",
            "Severe infection can reduce functional leaf area"
        ],

        "management": [
            "Use resistant or tolerant varieties where available.",
            "Maintain appropriate crop rotation where practical.",
            "Manage crop residue according to local recommendations.",
            "Monitor fields during favorable weather.",
            "Use locally approved fungicide programs when justified."
        ],

        "prevention": [
            "Use suitable resistant varieties.",
            "Monitor crops regularly.",
            "Follow recommended crop rotation practices.",
            "Manage infected crop residue appropriately."
        ]
    },


    "Corn_(maize)___Common_rust_": {
        "plant": "Corn",
        "disease": "Common Rust",
        "category": "Fungal disease",

        "description": (
            "Common rust is a fungal disease that produces rust-colored "
            "pustules on corn leaves."
        ),

        "symptoms": [
            "Small reddish-brown rust-colored pustules",
            "Pustules on both leaf surfaces",
            "Yellowing around heavily affected tissue",
            "Severe infection can reduce photosynthetic leaf area"
        ],

        "management": [
            "Monitor crops for rust pustules.",
            "Use resistant hybrids where available.",
            "Maintain appropriate crop management.",
            "Follow local recommendations for fungicide use when needed."
        ],

        "prevention": [
            "Use resistant varieties.",
            "Monitor crops regularly.",
            "Maintain good crop health."
        ]
    },


    "Corn_(maize)___Northern_Leaf_Blight": {
        "plant": "Corn",
        "disease": "Northern Leaf Blight",
        "category": "Fungal disease",

        "description": (
            "Northern leaf blight is a fungal disease characterized "
            "by large elongated lesions on corn leaves."
        ),

        "symptoms": [
            "Long gray-green or tan cigar-shaped lesions",
            "Lesions can enlarge over time",
            "Lower leaves may become heavily affected",
            "Severe disease can reduce photosynthetic capacity"
        ],

        "management": [
            "Use resistant hybrids where available.",
            "Monitor fields during cool and humid periods.",
            "Use appropriate crop rotation and residue management.",
            "Consider locally approved fungicide programs when necessary."
        ],

        "prevention": [
            "Use resistant hybrids.",
            "Maintain crop rotation.",
            "Manage crop residue appropriately.",
            "Monitor fields regularly."
        ]
    },


    "Corn_(maize)___healthy": {
        "plant": "Corn",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "corn leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal crop management.",
            "Monitor leaves regularly."
        ],

        "prevention": [
            "Maintain crop health.",
            "Monitor for new symptoms.",
            "Follow good field sanitation practices."
        ]
    },


    # ==========================================================
    # GRAPE
    # ==========================================================

    "Grape___Black_rot": {
        "plant": "Grape",
        "disease": "Black Rot",
        "category": "Fungal disease",

        "description": (
            "Grape black rot is a fungal disease that can affect "
            "leaves, shoots, and fruit."
        ),

        "symptoms": [
            "Brown circular leaf lesions",
            "Dark spots with defined margins",
            "Fruit may develop dark rot",
            "Black fruiting structures may develop on diseased tissue"
        ],

        "management": [
            "Remove infected fruit and plant debris.",
            "Improve canopy airflow.",
            "Prune appropriately to reduce dense foliage.",
            "Monitor developing fruit.",
            "Use locally approved disease-control products when necessary."
        ],

        "prevention": [
            "Maintain vineyard sanitation.",
            "Remove mummified fruit.",
            "Maintain good canopy airflow.",
            "Monitor regularly."
        ]
    },


    "Grape___Esca_(Black_Measles)": {
        "plant": "Grape",
        "disease": "Esca / Black Measles",
        "category": "Fungal disease complex",

        "description": (
            "Esca is a disease complex of grapevines associated with "
            "wood-inhabiting fungi and can produce characteristic leaf symptoms."
        ),

        "symptoms": [
            "Interveinal leaf discoloration",
            "Striped or scorched leaf patterns",
            "Dark spotting on fruit may occur",
            "Affected vines may gradually decline"
        ],

        "management": [
            "Remove and manage severely affected wood according to local guidance.",
            "Avoid unnecessary wounds to vines.",
            "Maintain healthy vineyard management practices.",
            "Consult local viticulture specialists for persistent cases."
        ],

        "prevention": [
            "Protect pruning wounds where locally recommended.",
            "Use healthy planting material.",
            "Remove severely affected material appropriately.",
            "Monitor vines regularly."
        ]
    },


    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "plant": "Grape",
        "disease": "Leaf Blight / Isariopsis Leaf Spot",
        "category": "Fungal disease",

        "description": (
            "This fungal leaf disease can produce dark lesions and "
            "blighting on grape foliage."
        ),

        "symptoms": [
            "Dark brown or black leaf spots",
            "Lesions may enlarge and merge",
            "Affected tissue may become necrotic",
            "Severe infection can cause premature leaf loss"
        ],

        "management": [
            "Remove heavily affected plant debris.",
            "Improve canopy airflow.",
            "Monitor foliage during favorable weather.",
            "Use locally approved disease-management products when required."
        ],

        "prevention": [
            "Maintain vineyard sanitation.",
            "Avoid excessive canopy density.",
            "Monitor foliage regularly."
        ]
    },


    "Grape___healthy": {
        "plant": "Grape",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "grape leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal vineyard care.",
            "Monitor leaves and fruit regularly."
        ],

        "prevention": [
            "Maintain canopy airflow.",
            "Maintain vineyard sanitation.",
            "Inspect vines regularly."
        ]
    },


    # ==========================================================
    # ORANGE
    # ==========================================================

    "Orange___Haunglongbing_(Citrus_greening)": {
        "plant": "Orange / Citrus",
        "disease": "Huanglongbing (Citrus Greening)",
        "category": "Bacterial disease",

        "description": (
            "Huanglongbing, commonly called citrus greening, is a serious "
            "citrus disease associated with bacteria and insect vectors."
        ),

        "symptoms": [
            "Blotchy or uneven leaf yellowing",
            "Yellow shoots",
            "Leaf mottling that may not follow veins symmetrically",
            "Fruit may become small or poorly colored",
            "Declining tree vigor"
        ],

        "management": [
            "Confirm suspected cases with appropriate agricultural diagnostic services.",
            "Monitor and manage insect vectors according to local recommendations.",
            "Use certified disease-free planting material.",
            "Follow local citrus disease-management regulations.",
            "Remove or manage infected trees according to regional guidance."
        ],

        "prevention": [
            "Use certified healthy planting material.",
            "Monitor citrus regularly.",
            "Manage vector populations according to local recommendations.",
            "Follow regional citrus disease regulations."
        ]
    },


    # ==========================================================
    # PEACH
    # ==========================================================

    "Peach___Bacterial_spot": {
        "plant": "Peach",
        "disease": "Bacterial Spot",
        "category": "Bacterial disease",

        "description": (
            "Bacterial spot is a disease that can affect peach leaves "
            "and fruit and is associated with bacterial infection."
        ),

        "symptoms": [
            "Small dark leaf spots",
            "Yellowing around some lesions",
            "Shot-hole appearance as damaged tissue drops out",
            "Fruit spots and surface blemishes"
        ],

        "management": [
            "Remove severely affected plant material where appropriate.",
            "Avoid unnecessary overhead irrigation.",
            "Maintain good tree vigor.",
            "Use resistant or tolerant varieties where available.",
            "Follow locally approved bacterial disease-management programs."
        ],

        "prevention": [
            "Use suitable varieties.",
            "Maintain good tree health.",
            "Avoid prolonged leaf wetness.",
            "Monitor foliage and fruit regularly."
        ]
    },


    "Peach___healthy": {
        "plant": "Peach",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "peach leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal orchard care.",
            "Monitor leaves and fruit regularly."
        ],

        "prevention": [
            "Maintain tree health.",
            "Maintain sanitation.",
            "Monitor regularly."
        ]
    },


    # ==========================================================
    # PEPPER
    # ==========================================================

    "Pepper,_bell___Bacterial_spot": {
        "plant": "Bell Pepper",
        "disease": "Bacterial Spot",
        "category": "Bacterial disease",

        "description": (
            "Bacterial spot affects pepper foliage and fruit and can "
            "produce small dark lesions."
        ),

        "symptoms": [
            "Small dark leaf spots",
            "Yellow halos may occur",
            "Leaf damage can increase under favorable conditions",
            "Fruit may develop raised or scabby lesions"
        ],

        "management": [
            "Remove severely affected material where appropriate.",
            "Avoid unnecessary overhead irrigation.",
            "Use disease-free seed and transplants.",
            "Improve air circulation around plants.",
            "Follow locally approved management recommendations."
        ],

        "prevention": [
            "Use clean planting material.",
            "Avoid handling wet plants.",
            "Maintain appropriate spacing.",
            "Practice crop sanitation."
        ]
    },


    "Pepper,_bell___healthy": {
        "plant": "Bell Pepper",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "bell pepper leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal crop care.",
            "Monitor foliage regularly."
        ],

        "prevention": [
            "Maintain sanitation.",
            "Avoid unnecessary leaf wetness.",
            "Monitor plants regularly."
        ]
    },


    # ==========================================================
    # POTATO
    # ==========================================================

    "Potato___Early_blight": {
        "plant": "Potato",
        "disease": "Early Blight",
        "category": "Fungal disease",

        "description": (
            "Early blight is a fungal disease that commonly produces "
            "dark lesions with characteristic concentric patterns on potato leaves."
        ),

        "symptoms": [
            "Dark brown leaf lesions",
            "Concentric ring patterns may appear",
            "Yellowing around older lesions",
            "Lower leaves are often affected first"
        ],

        "management": [
            "Remove heavily affected foliage where practical.",
            "Maintain adequate plant nutrition and vigor.",
            "Avoid prolonged leaf wetness.",
            "Use resistant or tolerant varieties where available.",
            "Follow locally approved fungicide recommendations when required."
        ],

        "prevention": [
            "Use healthy planting material.",
            "Practice crop rotation where appropriate.",
            "Maintain good plant nutrition.",
            "Monitor lower foliage regularly."
        ]
    },


    "Potato___Late_blight": {
        "plant": "Potato",
        "disease": "Late Blight",
        "category": "Oomycete disease",

        "description": (
            "Late blight is a destructive disease of potato that can "
            "develop rapidly under cool and wet conditions."
        ),

        "symptoms": [
            "Dark water-soaked leaf lesions",
            "Rapid expansion of affected tissue",
            "Brown or black foliage",
            "White growth may occur under humid conditions",
            "Tubers may also become infected"
        ],

        "management": [
            "Monitor plants frequently during cool and wet conditions.",
            "Remove severely affected plant material according to local guidance.",
            "Avoid moving infected material between fields.",
            "Use locally approved late-blight management programs.",
            "Follow agricultural extension recommendations for severe outbreaks."
        ],

        "prevention": [
            "Use certified healthy seed tubers.",
            "Monitor weather and disease conditions.",
            "Maintain field sanitation.",
            "Use resistant varieties where available."
        ]
    },


    "Potato___healthy": {
        "plant": "Potato",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "potato leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal crop care.",
            "Monitor foliage regularly."
        ],

        "prevention": [
            "Use healthy planting material.",
            "Maintain crop sanitation.",
            "Monitor plants regularly."
        ]
    },


    # ==========================================================
    # RASPBERRY
    # ==========================================================

    "Raspberry___healthy": {
        "plant": "Raspberry",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "raspberry leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue routine plant care.",
            "Monitor leaves and fruit regularly."
        ],

        "prevention": [
            "Maintain sanitation.",
            "Maintain adequate airflow.",
            "Inspect plants regularly."
        ]
    },


    # ==========================================================
    # SOYBEAN
    # ==========================================================

    "Soybean___healthy": {
        "plant": "Soybean",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "soybean leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal crop management.",
            "Monitor plants regularly."
        ],

        "prevention": [
            "Maintain crop health.",
            "Monitor fields regularly.",
            "Follow good crop management practices."
        ]
    },


    # ==========================================================
    # SQUASH
    # ==========================================================

    "Squash___Powdery_mildew": {
        "plant": "Squash",
        "disease": "Powdery Mildew",
        "category": "Fungal disease",

        "description": (
            "Powdery mildew is a common fungal disease that produces "
            "white powder-like growth on squash leaves."
        ),

        "symptoms": [
            "White powdery patches on leaves",
            "Yellowing of affected foliage",
            "Reduced leaf function",
            "Premature leaf decline in severe cases"
        ],

        "management": [
            "Improve airflow around plants.",
            "Remove severely affected leaves where appropriate.",
            "Avoid unnecessarily dense foliage.",
            "Use locally approved powdery mildew treatments when required."
        ],

        "prevention": [
            "Provide adequate spacing.",
            "Maintain airflow.",
            "Monitor foliage frequently.",
            "Avoid excessive canopy humidity."
        ]
    },


    # ==========================================================
    # STRAWBERRY
    # ==========================================================

    "Strawberry___Leaf_scorch": {
        "plant": "Strawberry",
        "disease": "Leaf Scorch",
        "category": "Fungal disease",

        "description": (
            "Leaf scorch can produce dark lesions and scorched areas "
            "on strawberry foliage."
        ),

        "symptoms": [
            "Dark purple to brown leaf spots",
            "Scorched-looking leaf tissue",
            "Lesions may merge as disease progresses",
            "Affected leaves may decline prematurely"
        ],

        "management": [
            "Remove heavily affected leaves where appropriate.",
            "Maintain good field sanitation.",
            "Avoid prolonged leaf wetness.",
            "Improve airflow around plants.",
            "Follow local disease-management recommendations."
        ],

        "prevention": [
            "Maintain sanitation.",
            "Avoid excessive plant density.",
            "Monitor leaves regularly.",
            "Use healthy planting material."
        ]
    },


    "Strawberry___healthy": {
        "plant": "Strawberry",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "strawberry leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal crop care.",
            "Monitor foliage and fruit."
        ],

        "prevention": [
            "Maintain sanitation.",
            "Maintain good airflow.",
            "Monitor plants regularly."
        ]
    },


    # ==========================================================
    # TOMATO
    # ==========================================================

    "Tomato___Bacterial_spot": {
        "plant": "Tomato",
        "disease": "Bacterial Spot",
        "category": "Bacterial disease",

        "description": (
            "Bacterial spot is a disease of tomato foliage and fruit "
            "that produces small dark lesions."
        ),

        "symptoms": [
            "Small dark spots on leaves",
            "Yellow halos may surround lesions",
            "Leaf damage can increase over time",
            "Dark spots may develop on fruit"
        ],

        "management": [
            "Remove severely affected plant material where appropriate.",
            "Avoid unnecessary overhead irrigation.",
            "Use clean seed and planting material.",
            "Maintain appropriate plant spacing.",
            "Follow locally approved bacterial disease-management practices."
        ],

        "prevention": [
            "Use disease-free planting material.",
            "Avoid handling wet foliage.",
            "Maintain sanitation.",
            "Rotate crops where appropriate."
        ]
    },


    "Tomato___Early_blight": {
        "plant": "Tomato",
        "disease": "Early Blight",
        "category": "Fungal disease",

        "description": (
            "Tomato early blight is a fungal disease that commonly "
            "produces dark lesions with concentric rings."
        ),

        "symptoms": [
            "Dark brown circular lesions",
            "Concentric ring patterns",
            "Yellowing around affected areas",
            "Lower leaves often become affected first"
        ],

        "management": [
            "Remove severely affected lower leaves where appropriate.",
            "Improve airflow around plants.",
            "Avoid prolonged leaf wetness.",
            "Maintain adequate plant nutrition.",
            "Use locally approved disease-control products when required."
        ],

        "prevention": [
            "Rotate crops where appropriate.",
            "Remove infected plant debris.",
            "Maintain plant spacing.",
            "Water plants in ways that minimize prolonged leaf wetness."
        ]
    },


    "Tomato___Late_blight": {
        "plant": "Tomato",
        "disease": "Late Blight",
        "category": "Oomycete disease",

        "description": (
            "Tomato late blight can progress rapidly under cool and "
            "wet conditions and may affect leaves, stems, and fruit."
        ),

        "symptoms": [
            "Dark water-soaked leaf lesions",
            "Rapidly expanding brown or black tissue",
            "White growth may appear under humid conditions",
            "Fruit may develop dark lesions"
        ],

        "management": [
            "Monitor plants frequently during favorable weather.",
            "Remove affected plant material according to local guidance.",
            "Avoid spreading infected material.",
            "Use locally approved late-blight management programs.",
            "Seek local agricultural guidance during severe outbreaks."
        ],

        "prevention": [
            "Use healthy planting material.",
            "Monitor disease conditions.",
            "Maintain good airflow.",
            "Remove infected debris appropriately."
        ]
    },


    "Tomato___Leaf_Mold": {
        "plant": "Tomato",
        "disease": "Leaf Mold",
        "category": "Fungal disease",

        "description": (
            "Tomato leaf mold is a fungal disease that is favored by "
            "high humidity and can produce yellow areas on the upper "
            "leaf surface and fungal growth underneath."
        ),

        "symptoms": [
            "Yellow patches on upper leaf surfaces",
            "Olive-green or brown fungal growth underneath leaves",
            "Leaves may curl or decline",
            "Severe disease can reduce leaf function"
        ],

        "management": [
            "Improve ventilation and airflow.",
            "Reduce prolonged high humidity where practical.",
            "Remove heavily affected leaves.",
            "Avoid unnecessary leaf wetness.",
            "Use locally approved treatments when necessary."
        ],

        "prevention": [
            "Improve greenhouse or canopy ventilation.",
            "Maintain appropriate spacing.",
            "Avoid prolonged foliage wetness.",
            "Monitor lower leaf surfaces."
        ]
    },


    "Tomato___Septoria_leaf_spot": {
        "plant": "Tomato",
        "disease": "Septoria Leaf Spot",
        "category": "Fungal disease",

        "description": (
            "Septoria leaf spot is a fungal disease that produces "
            "small circular lesions, often beginning on older leaves."
        ),

        "symptoms": [
            "Small circular leaf spots",
            "Dark margins around lesions",
            "Light centers may develop",
            "Tiny dark structures may appear in lesion centers",
            "Lower leaves are commonly affected first"
        ],

        "management": [
            "Remove heavily affected lower leaves.",
            "Remove infected plant debris.",
            "Improve airflow.",
            "Avoid unnecessary overhead irrigation.",
            "Use locally approved fungicide programs when required."
        ],

        "prevention": [
            "Maintain crop sanitation.",
            "Rotate crops where appropriate.",
            "Keep foliage as dry as practical.",
            "Monitor lower leaves regularly."
        ]
    },


    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "plant": "Tomato",
        "disease": "Two-Spotted Spider Mite Damage",
        "category": "Arthropod pest",

        "description": (
            "Two-spotted spider mites are tiny plant-feeding pests that "
            "can cause stippling and discoloration of tomato leaves."
        ),

        "symptoms": [
            "Fine yellow or pale stippling",
            "Bronzing or general leaf discoloration",
            "Fine webbing may be visible in heavier infestations",
            "Leaves may dry and decline"
        ],

        "management": [
            "Inspect the undersides of leaves carefully.",
            "Reduce plant stress where possible.",
            "Use appropriate biological or locally approved pest-management methods.",
            "Avoid unnecessary broad-spectrum pesticide use that can disrupt beneficial organisms.",
            "Follow local integrated pest-management recommendations."
        ],

        "prevention": [
            "Monitor leaves regularly.",
            "Maintain adequate plant health.",
            "Check leaf undersides for pests.",
            "Encourage beneficial organisms where appropriate."
        ]
    },


    "Tomato___Target_Spot": {
        "plant": "Tomato",
        "disease": "Target Spot",
        "category": "Fungal disease",

        "description": (
            "Target spot is a fungal disease that produces circular "
            "lesions with concentric patterns on tomato foliage and fruit."
        ),

        "symptoms": [
            "Circular brown lesions",
            "Concentric target-like rings",
            "Leaf yellowing",
            "Fruit lesions may develop"
        ],

        "management": [
            "Remove severely affected leaves where appropriate.",
            "Improve airflow.",
            "Avoid prolonged foliage wetness.",
            "Maintain plant nutrition and vigor.",
            "Use locally approved disease-management products when necessary."
        ],

        "prevention": [
            "Maintain plant spacing.",
            "Remove infected debris.",
            "Monitor foliage regularly.",
            "Avoid unnecessary leaf wetness."
        ]
    },


    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "plant": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus",
        "category": "Viral disease",

        "description": (
            "Tomato yellow leaf curl virus is a viral disease that can "
            "cause yellowing, curling, and reduced growth. It is commonly "
            "associated with whitefly transmission."
        ),

        "symptoms": [
            "Upward curling of leaves",
            "Yellowing of leaf tissue",
            "Reduced plant growth",
            "Small or poorly developed plants",
            "Reduced fruit production"
        ],

        "management": [
            "Monitor and manage whitefly populations according to local IPM guidance.",
            "Remove severely affected plants where recommended.",
            "Use resistant or tolerant varieties where available.",
            "Use healthy planting material.",
            "Control weeds that may serve as alternative hosts where appropriate."
        ],

        "prevention": [
            "Use resistant varieties where available.",
            "Use healthy seedlings.",
            "Monitor for whiteflies.",
            "Maintain field sanitation."
        ]
    },


    "Tomato___Tomato_mosaic_virus": {
        "plant": "Tomato",
        "disease": "Tomato Mosaic Virus",
        "category": "Viral disease",

        "description": (
            "Tomato mosaic virus can cause characteristic mosaic patterns "
            "and may reduce plant growth and productivity."
        ),

        "symptoms": [
            "Light and dark green mosaic patterns",
            "Leaf distortion",
            "Reduced plant vigor",
            "Fruit development may be affected"
        ],

        "management": [
            "Remove severely infected plants where recommended.",
            "Avoid spreading plant sap between plants.",
            "Clean tools and equipment appropriately.",
            "Use certified healthy seed and planting material.",
            "Follow local virus-management recommendations."
        ],

        "prevention": [
            "Use clean planting material.",
            "Disinfect tools appropriately.",
            "Avoid unnecessary plant-to-plant contact.",
            "Maintain good sanitation."
        ]
    },


    "Tomato___healthy": {
        "plant": "Tomato",
        "disease": "Healthy",
        "category": "Healthy",

        "description": (
            "The model classified the image as an apparently healthy "
            "tomato leaf."
        ),

        "symptoms": [
            "No strong visual evidence of the supported diseases"
        ],

        "management": [
            "Continue normal tomato plant care.",
            "Monitor leaves and stems regularly."
        ],

        "prevention": [
            "Maintain sanitation.",
            "Monitor plants regularly.",
            "Maintain good airflow.",
            "Use healthy planting material."
        ]
    }
}


# ==============================================================
# FALLBACK INFORMATION
# ==============================================================

DEFAULT_DISEASE_INFORMATION = {

    "plant": "Unknown",

    "disease": "Unknown condition",

    "category": "Unknown",

    "description": (
        "The model identified a supported PlantVillage class, "
        "but detailed information for this class is not currently "
        "available in the knowledge base."
    ),

    "symptoms": [
        "The prediction should be treated as an AI-assisted result.",
        "Inspect the plant carefully for visible symptoms."
    ],

    "management": [
        "Avoid making treatment decisions based only on the AI prediction.",
        "Inspect the plant and surrounding plants carefully.",
        "Consult a local agricultural expert if symptoms persist or worsen."
    ],

    "prevention": [
        "Maintain good plant hygiene.",
        "Monitor plants regularly.",
        "Use healthy planting material where possible."
    ]
}


def get_disease_information(class_name: str) -> dict:
    """
    Return structured information for a predicted class.

    Parameters
    ----------
    class_name : str
        Exact CNN class name.

    Returns
    -------
    dict
        Disease information.
    """

    return DISEASE_INFORMATION.get(
        class_name,
        DEFAULT_DISEASE_INFORMATION
    )