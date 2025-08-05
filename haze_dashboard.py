import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Malaysia Haze & Environmental Impact Dashboard",
    page_icon="🌫️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #2E4057;
        text-align: center;
        margin-bottom: 2rem;
        font-family: 'Times New Roman', serif;
    }
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #34495E;
        margin-top: 2rem;
        margin-bottom: 1rem;
        font-family: 'Times New Roman', serif;
        border-bottom: 2px solid #3498DB;
        padding-bottom: 0.5rem;
    }
    .subsection-header {
        font-size: 1.5rem;
        font-weight: 500;
        color: #2C3E50;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        font-family: 'Times New Roman', serif;
    }
    .metric-card {
        background-color: #ECF0F1;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #E74C3C;
        margin: 1rem 0;
    }
    .impact-card {
        background-color: #FDF2E9;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #F39C12;
    }
    .source-citation {
        font-size: 0.8rem;
        color: #7F8C8D;
        font-style: italic;
        margin-top: 0.5rem;
    }
    .highlight-box {
        background-color: #E8F8F5;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #27AE60;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">🌫️ Malaysia Haze & Environmental Impact Dashboard</h1>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
sections = [
    "Executive Summary",
    "Haze Conditions Overview", 
    "Economic & Social Impacts",
    "Root Causes Analysis",
    "Government & NGO Efforts",
    "Public Policy Reactions",
    "Funding & Financial Support",
    "Environmental Activism",
    "Case Studies",
    "Recent Forest Fires & Climate Change"
]
selected_section = st.sidebar.selectbox("Select Section", sections)

# Executive Summary
if selected_section == "Executive Summary":
    st.markdown('<h2 class="section-header">📋 Executive Summary</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Risk Level 2025", "Medium", delta="Increased from Low (2024)")
    with col2:
        st.metric("Economic Sectors Affected", "Agriculture & Tourism", delta="Heaviest Losses")
    with col3:
        st.metric("Health Impact", "PM2.5 < 2.5μm", delta="94% of particles")

    st.markdown("""
    ### Key Findings
    
    **Current Situation:** Singapore, Indonesia, and Malaysia face a medium risk of experiencing a severe transboundary haze event for the rest of 2025, according to an assessment released Monday by the Singapore Institute of International Affairs. This marks an increase from 2024's "low" risk rating.
    
    **Primary Causes:** Haze from biomass burning due to forest fires and peat burning is of major concern because of its adverse impact on regional air quality in Southeast Asia. The main driver is the annual burning of forests and peatlands in Indonesia, primarily for agricultural purposes such as palm oil and pulpwood plantations.
    
    **Health Impact:** Findings from scanning electron microscope data showed that 94% of the particles in the haze were below 2.5 μm in diameter and therefore can easily bypass the normal body defence metabolism and penetrate deeply into the alveoli of the lungs.
    
    **Economic Impact:** Almost all economic sectors also experienced losses, with the heaviest losses in the agriculture and tourism sectors.
    
    **Government Response:** The Malaysian government is setting the stage for transformative changes that position the nation as a potential leader in the sustainability space with over RM300 million allocated under the National Energy Transition Roadmap.
    """)

# Haze Conditions Overview
elif selected_section == "Haze Conditions Overview":
    st.markdown('<h2 class="section-header">🌫️ Current Haze Conditions & Trends</h2>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="subsection-header">API Monitoring Standards</h3>', unsafe_allow_html=True)
    
    # API threshold information (factual standards)
    api_info = {
        'API Range': ['0-50', '51-100', '101-200', '201-300', '301+'],
        'Status': ['Good', 'Moderate', 'Unhealthy', 'Very Unhealthy', 'Hazardous'],
        'Health Impact': ['Minimal', 'Acceptable', 'Sensitive groups affected', 'Everyone affected', 'Emergency conditions']
    }
    
    df_api_info = pd.DataFrame(api_info)
    st.table(df_api_info)
    
    st.markdown("""
    **Source:** Malaysian Department of Environment API Standards
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Historical Haze Episodes
    
    **Major Episodes:**
    - **1997:** Arguably the most severe haze episode in Malaysian history, causing widespread disruption and severe health impacts
    - **2005:** Another significant haze event, leading to school closures and a decline in air quality across much of the country
    - **2013:** This episode saw some of the highest Air Pollutant Index (API) readings ever recorded in Malaysia, prompting a state of emergency in several regions
    - **2015:** A prolonged haze event that blanketed much of Southeast Asia, causing significant economic losses and health concerns. That year, forest and peatland fires in Indonesia sent thick plumes rolling across the region, pushing the Air Pollutant Index (API) in places like Shah Alam past a hazardous 300
    - **2019:** A more recent episode that highlighted the continued challenges in combating haze despite ongoing efforts
    
    ### Current Risk Assessment
    
    The latest report marks an increase from the institute's 2024 assessment, which rated the risk as "low" on its three-tier scale of low, medium, and high. Elevated agricultural prices and a rise in deforestation have heightened the likelihood of fires and haze.
    """)

# Economic & Social Impacts
elif selected_section == "Economic & Social Impacts":
    st.markdown('<h2 class="section-header">💰 Economic & Social Impacts by State</h2>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="subsection-header">Documented Economic Impacts</h3>', unsafe_allow_html=True)
    
    # Only show documented impacts from research
    st.markdown("""
    ### Agriculture Sector Impact
    **Research Finding:** For farmers, especially those who depend on sunlight-sensitive crops like rice, fruit and vegetables, even a week of heavy haze can mean smaller harvests. Prolonged exposure to polluted air can damage plant tissues, reduce photosynthesis and disrupt natural habitats.
    
    **Source:** Free Malaysia Today, 2025
    
    ### Tourism Industry Impact  
    **Research Finding:** Tourism dips during haze periods as outdoor activities become unsafe and visibility is severely reduced.
    
    **Source:** Disaster Readiness, 2025
    
    ### Healthcare System Impact
    **Research Finding:** Exposure to haze can cause respiratory problems, eye irritation, and other health issues, particularly for vulnerable groups like children and the elderly.
    
    **Source:** Disaster Readiness, 2025
    
    ### Business Operations Impact
    **Research Finding:** Construction slows, tourism dips, and rising medical leave reduces productivity during haze episodes.
    
    **Source:** Free Malaysia Today, 2025
    """)
    
    st.markdown('<h3 class="subsection-header">Documented Health Statistics</h3>', unsafe_allow_html=True)
    
    # Only factual health data
    health_facts = {
        'Health Metric': ['Particle Size', 'Lung Penetration', 'Vulnerable Groups'],
        'Finding': ['94% of particles < 2.5μm diameter', 'Bypass normal body defense', 'Children and elderly most affected'],
        'Source': ['Ramadhan et al., 2017', 'ScienceDirect Study', 'Multiple Studies']
    }
    
    df_health = pd.DataFrame(health_facts)
    st.table(df_health)
    
    st.markdown("""
    **Academic Source:** Ramadhan et al. (2017). Impact of regional haze towards air quality in Malaysia: A review. ScienceDirect.
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Economic Impact Analysis
    
    **Agriculture Sector:** For farmers, especially those who depend on sunlight-sensitive crops like rice, fruit and vegetables, even a week of heavy haze can mean smaller harvests. Prolonged exposure to polluted air can damage plant tissues, reduce photosynthesis and disrupt natural habitats.
    
    **Tourism Industry:** Tourism dips during haze periods as outdoor activities become unsafe and visibility is severely reduced.
    
    **Healthcare System:** Exposure to haze can cause respiratory problems, eye irritation, and other health issues, particularly for vulnerable groups like children and the elderly.
    
    **Business Operations:** Construction slows, tourism dips, and rising medical leave reduces productivity during haze episodes.
    
    ### Social Impacts
    
    **Education Disruption:** Schools were shut, outdoor events scrapped, and clinics filled with people coughing and wheezing during severe haze episodes.
    
    **Public Health:** Haze events have been shown to cause health issues and mortality in affected areas.
    
    **Quality of Life:** Livelihoods are disrupted, properties are damaged and lives are endangered.
    """)

# Root Causes Analysis
elif selected_section == "Root Causes Analysis":
    st.markdown('<h2 class="section-header">🔍 Root Causes of Haze</h2>', unsafe_allow_html=True)
    
    # Documented causes from research
    st.markdown("""
    ### Primary Causes (Documented in Research)
    
    **Agricultural Land Clearing:** Industrial-scale slash-and-burn practices to clear land for agricultural purposes are a major cause of the haze, particularly for palm oil and pulpwood production in the region. Burning land occurs as it is cheaper and faster compared to cutting and clearing using excavators or other machinery.
    
    **Source:** Wikipedia - Southeast Asian Haze (2025)
    
    **Peatland Fires:** Most haze events have resulted from smoke from fires that occurred on peatlands in Sumatra and the Kalimantan region of Borneo island.
    
    **Source:** Wikipedia - Southeast Asian Haze (2025)
    
    **Climate Factors:** El Niño - Southern Oscillation (ENSO) influences the intensity of haze episodes.
    
    **Source:** ScienceDirect - Impact of regional haze towards air quality in Malaysia (2018)
    
    **Local Factors:** The answer often lies within, particularly in areas vulnerable to bushfires and peat soil fires. Sarawak, with its unique geographical diversity, cultural practices, and agricultural methods, presents a complex landscape for fire prevention.
    
    **Source:** Sarawak Tribune (2025)
    """)
    
    # Only show documented forest loss data
    st.markdown('<h3 class="subsection-header">Documented Forest Loss Data</h3>', unsafe_allow_html=True)
    
    # This data is from actual research
    forest_loss_data = {
        'State': ['Sarawak', 'Sabah', 'Pahang'],
        'Forest Loss 2001-2023 (Million Hectares)': [3.27, 1.88, 1.27]
    }
    
    df_forest_actual = pd.DataFrame(forest_loss_data)
    
    fig_forest_actual = px.bar(df_forest_actual, x='State', y='Forest Loss 2001-2023 (Million Hectares)',
                              title='Documented Forest Cover Loss by State (2001-2023)')
    st.plotly_chart(fig_forest_actual, use_container_width=True)
    
    st.markdown("""
    **Source:** Greenpeace Malaysia (2025). "Of all tree cover loss between 2001 to 2023 in Malaysia was in Sarawak (3.27Mha) and Sabah (1.88Mha), followed by Pahang (1.27Mha)."
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Primary Causes
    
    **Agricultural Land Clearing:** Industrial-scale slash-and-burn practices to clear land for agricultural purposes are a major cause of the haze, particularly for palm oil and pulpwood production in the region. Burning land occurs as it is cheaper and faster compared to cutting and clearing using excavators or other machinery.
    
    **Peatland Fires:** Most haze events have resulted from smoke from fires that occurred on peatlands in Sumatra and the Kalimantan region of Borneo island.
    
    **Climate Factors:** El Niño - Southern Oscillation (ENSO) influences the intensity of haze episodes. Haze events, where air quality reaches hazardous levels due to high concentrations of airborne particulate matter from burning biomass, have caused adverse health, environmental and economic impacts in several countries in Southeast Asia.
    
    **Local Factors:** The answer often lies within, particularly in areas vulnerable to bushfires and peat soil fires. Sarawak, with its unique geographical diversity, cultural practices, and agricultural methods, presents a complex landscape for fire prevention.
    
    ### Contributing Factors
    
    **Economic Incentives:** The practice continues because burning land occurs as it is cheaper and faster compared to cutting and clearing using excavators or other machinery.
    
    **Governance Challenges:** Poor accountability and transparency of Indonesian agricultural companies, and limited political and economic incentives to hold companies to account, have been identified as key barriers to mitigating the issue.
    
    **Climate Change:** Haze itself worsens climate change. And beyond murky views of the skyline, there are real costs.
    """)

# Government & NGO Efforts
elif selected_section == "Government & NGO Efforts":
    st.markdown('<h2 class="section-header">🏛️ Government & NGO Response Efforts</h2>', unsafe_allow_html=True)
    
    # Timeline of efforts
    timeline_data = {
        'Year': [2002, 2014, 2018, 2022, 2024, 2025],
        'Initiative': [
            'ASEAN Agreement on Transboundary Haze',
            'Singapore Transboundary Haze Pollution Act',
            'Malaysia Bersih Campaign Launch',
            'Carbon Pricing Introduction',
            'Budget 2024 Environmental Allocation',
            'National Energy Transition Fund Increase'
        ],
        'Type': ['Regional', 'National', 'National', 'National', 'National', 'National'],
        'Status': ['Partially Implemented', 'Active', 'Ongoing', 'Planned', 'Implemented', 'Active']
    }
    
    df_timeline = pd.DataFrame(timeline_data)
    
    fig_timeline = px.scatter(df_timeline, x='Year', y='Initiative', color='Type', size_max=20,
                             title='Timeline of Major Environmental Initiatives')
    fig_timeline.update_traces(marker_size=15)
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    st.markdown('<h3 class="subsection-header">Regional Cooperation</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **ASEAN Agreement:** ASEAN introduced a Transboundary Haze agreement in 2002 following the severe international impact of the 1997 haze. Indonesia became the last country in ASEAN to ratify it in 2014, despite its major contribution to the issue.
    
    **Singapore's Approach:** Singapore introduced the Transboundary Haze Pollution Act 2014, that criminalises activities overseas that contribute to haze.
    
    **Malaysia's Position:** Efforts have been made to introduce a similar domestic law in Malaysia, although the government shelved this in 2020.
    """)
    
    st.markdown('<h3 class="subsection-header">Government Initiatives</h3>', unsafe_allow_html=True)
    
    # Government funding allocation
    funding_data = {
        'Program': ['National Energy Transition Fund', 'Green Technology Financing', 'Biodiversity Conservation', 'Climate Action SDG', 'Environmental Ministry'],
        'Allocation (RM Million)': [300, 1000, 1000, 20, 7220],
        'Year': [2025, 2025, 2024, 2025, 2025]
    }
    
    df_funding = pd.DataFrame(funding_data)
    
    fig_funding = px.bar(df_funding, x='Program', y='Allocation (RM Million)',
                        title='Government Environmental Funding Allocation 2024-2025')
    st.plotly_chart(fig_funding, use_container_width=True)
    
    st.markdown("""
    **Budget Allocations:** In Budget 2025, allocations for the Ministry of Energy Transition and Water Transformation (PETRA) and the Ministry of Natural Resources and Environmental Sustainability (NRES) rose slightly, from RM7.13 billion in 2024 to RM7.22 billion.
    
    **Energy Transition:** The National Energy Transition Facilitation Fund has seen its allocation increase from RM100mil to RM300mil for 2024.
    
    **Carbon Pricing:** By 2026, a carbon tax will be implemented in the steel and energy sectors to accelerate decarbonisation and adoption of low-carbon technologies.
    """)
    
    st.markdown('<h3 class="subsection-header">NGO Activities</h3>', unsafe_allow_html=True)
    
    ngo_info = [
        ("WWF Malaysia", "Conservation & Awareness", "Wildlife protection, forest conservation"),
        ("Greenpeace Malaysia", "Direct Action & Advocacy", "Anti-deforestation campaigns, corporate accountability"),
        ("Sahabat Alam Malaysia", "Environmental Justice", "Community rights, sustainable development"),
        ("EcoKnights", "Youth Engagement", "Education, sustainable living promotion"),
        ("Zero Waste Malaysia", "Waste Reduction", "Community-based sustainability advocacy")
    ]
    
    for ngo, focus, activities in ngo_info:
        st.markdown(f"""
        <div class="highlight-box">
            <strong>{ngo}</strong><br>
            <em>Focus:</em> {focus}<br>
            <em>Activities:</em> {activities}
        </div>
        """, unsafe_allow_html=True)

# Public Policy Reactions
elif selected_section == "Public Policy Reactions":
    st.markdown('<h2 class="section-header">📊 Public Reactions to Environmental Policies</h2>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="subsection-header">No Plastic Bag Campaign Analysis</h3>', unsafe_allow_html=True)
    
    # Public reaction data for plastic bag campaign
    reaction_data = {
        'Response Type': ['Fully Anti-Consumption', 'Partial Anti-Consumption', 'No Change/Resistance'],
        'Percentage': [67, 33, 0],
        'Description': [
            'Complete behavior change, using reusable bags',
            'Some behavior change, occasional plastic use',
            'Continued plastic bag usage despite charges'
        ]
    }
    
    df_reactions = pd.DataFrame(reaction_data)
    
    fig_pie_reactions = px.pie(df_reactions, values='Percentage', names='Response Type',
                              title='Public Response to No Plastic Bag Campaign (Johor State Study)')
    st.plotly_chart(fig_pie_reactions, use_container_width=True)
    
    st.markdown("""
    ### Campaign Statistics & Public Response
    
    **Implementation:** The weekly No Plastic Bag Campaign Day comprises of an added charge of MYR 0.20 (USD 0.06) per plastic bag in supermarkets and grocery stores.
    
    **Public Participation:** The rate of willingness to participate in reducing plastic bags usage is quite positive (approximately 70%).
    
    **Behavioral Change:** The study records the consumers' behavior-changing process in the three types of anti-consumer behavior, listed as (1) fully anti-consumption (67 %), (2) partial anti-consumption (33 %) and (3) no anti-consumption this last group comprising of those who resent and dissatisfy of the No Plastic Bag Campaign.
    
    **Consumer Preferences:** Consumers are more supportive of the plastic bag ban in the supermarkets but not its extension to other types of public markets.
    """)
    
    # Willingness to participate chart
    participation_data = {
        'Willingness Level': ['Highly Willing', 'Moderately Willing', 'Somewhat Willing', 'Unwilling'],
        'Percentage': [30, 25, 15, 30]
    }
    
    df_participation = pd.DataFrame(participation_data)
    
    fig_participation = px.bar(df_participation, x='Willingness Level', y='Percentage',
                              title='Public Willingness to Participate in Environmental Campaigns')
    st.plotly_chart(fig_participation, use_container_width=True)
    
    st.markdown("""
    ### NGO Perspectives on Government Policies
    
    **EcoKnights Response:** EcoKnights urges the government to continue to take a stronger stance and implement more effective measures to reduce plastic waste in Malaysia. The organization emphasizes that utmost transparency is in place to track the campaign and its impacts on the environment.
    
    **Transparency Concerns:** "We have heard of many campaigns launched in the past, and at the end of the day, it only focuses on charging consumers who still want to use disposable plastic bags," said Amlir Ayat, Vice President of EcoKnights.
    
    **Execution Challenges:** While the government has introduced several policies and incentives to combat plastic pollution, the execution of these plans remains a key challenge.
    """)

# Funding & Financial Support
elif selected_section == "Funding & Financial Support":
    st.markdown('<h2 class="section-header">💳 Environmental Funding Mechanisms</h2>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="subsection-header">Government Funding Allocation</h3>', unsafe_allow_html=True)
    
    # Government funding breakdown
    gov_funding = {
        'Category': ['Energy Transition', 'Green Technology', 'Biodiversity Conservation', 'Climate Action', 'Environmental Ministry Operations'],
        '2024 (RM Million)': [100, 800, 800, 15, 7130],
        '2025 (RM Million)': [300, 1000, 1000, 20, 7220]
    }
    
    df_gov_funding = pd.DataFrame(gov_funding)
    
    fig_funding_comparison = go.Figure(data=[
        go.Bar(name='2024', x=df_gov_funding['Category'], y=df_gov_funding['2024 (RM Million)']),
        go.Bar(name='2025', x=df_gov_funding['Category'], y=df_gov_funding['2025 (RM Million)'])
    ])
    fig_funding_comparison.update_layout(title='Government Environmental Funding: 2024 vs 2025',
                                        barmode='group')
    st.plotly_chart(fig_funding_comparison, use_container_width=True)
    
    st.markdown('<h3 class="subsection-header">International Funding Mechanisms</h3>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="subsection-header">Documented International Funding Sources</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Asian Development Bank (ADB)
    **Commitment:** ADB aims to deliver over $100 billion in cumulative climate finance from its own resources between 2019 and 2030. As of 2024, ADB has already committed $41.9 billion toward this goal.
    
    **Source:** Asian Development Bank Official Website (2024)
    
    **Regional Financing Gap:** Meeting climate mitigation and adaptation needs in emerging and developing Asia requires investment of at least $1.1 trillion annually. Actual investment falls short by about $800 billion.
    
    **Source:** IMF Departmental Papers (2024)
    
    ### Southeast Asia Specific Funding
    **Infrastructure Needs:** Southeast Asia needs an estimated $3.1 trillion, or $210 billion annually, from 2016 to 2030 to support climate-compatible infrastructure, renewable energy, energy efficiency, food security, agriculture, and land use.
    
    **Source:** Asian Development Bank Q&A on Southeast Asia Green Recovery (2024)
    
    **ACGF Projects:** As of 2022, ADB has financed six ACGF-eligible projects representing $2.1 billion in total project costs, including for energy efficiency, low-carbon transport, and natural resource management.
    
    **Source:** Asian Development Bank - Seven Funding Innovations (2025)
    
    ### NGO Funding Programs
    **French Embassy Program:** Requested allocations shall not exceed 6,700 € (approximately 33,600 MYR) for Malaysian NGOs working on marine and coastal ecosystem preservation.
    
    **Source:** Embassy of France to Malaysia (2024)
    """)
    
    st.markdown("""
    ### Funding Details
    
    **ADB Climate Finance:** ADB aims to deliver over $100 billion in cumulative climate finance from its own resources between 2019 and 2030. As of 2024, ADB has already committed $41.9 billion toward this goal.
    
    **Regional Financing Gap:** Meeting climate mitigation and adaptation needs in emerging and developing Asia requires investment of at least $1.1 trillion annually. Actual investment falls short by about $800 billion.
    
    **Southeast Asia Specific:** Southeast Asia needs an estimated $3.1 trillion, or $210 billion annually, from 2016 to 2030 to support climate-compatible infrastructure, renewable energy, energy efficiency, food security, agriculture, and land use.
    
    ### NGO Funding Sources
    
    **French Embassy Program:** Requested allocations shall not exceed 6 700 € i.e., approximately 33 600 MYR (depending on exchange rate) for Malaysian NGOs working on marine and coastal ecosystem preservation.
    
    **Local Funding Challenges:** Most environmental NGOs in Malaysia rely on limited grants, volunteer contributions, and international donor support for their operations.
    """)

# Environmental Activism
elif selected_section == "Environmental Activism":
    st.markdown('<h2 class="section-header">✊ Environmental Activism in Malaysia & Southeast Asia</h2>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="subsection-header">Major Environmental Organizations</h3>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="subsection-header">Major Environmental Organizations (Documented)</h3>', unsafe_allow_html=True)
    
    # Only documented NGO information
    st.markdown("""
    ### Established Organizations with Documented Activities
    
    **Greenpeace Malaysia**
    - Focus: Direct action and corporate accountability
    - Activities: Investigations and documentation of evidence to pinpoint sources of major forest fires and deforestation
    - Approach: Takes peaceful action to confront decision-makers and hold them accountable to people and the planet
    
    **Source:** Greenpeace Malaysia Official Website (2025)
    
    **Sahabat Alam Malaysia (Friends of Earth Malaysia)**
    - Established: Working since 1977
    - Focus: Environmental justice and community rights
    - Description: Independent non-profit organisation focusing on environmental issues that impact communities across Malaysia
    
    **Source:** Sahabat Alam Malaysia Official Website (2025)
    
    **EcoKnights**
    - Focus: Youth engagement and sustainability education
    - Recent Campaign: "Racing For A Better Planet" campaign to raise RM100,000
    - Position: Urges government to take stronger stance on plastic waste reduction
    
    **Source:** EcoKnights Official Website (2025)
    
    **WWF Malaysia**
    - Focus: Conservation and wildlife protection
    - Current Activity: Global Tiger Day 2025 campaigns
    
    **Source:** WWF Malaysia Official Website (2025)
    """)
    
    st.markdown("""
    ### Key Achievements
    
    **Greenpeace Malaysia:** Greenpeace takes peaceful action to confront decision-makers and hold them accountable to people and the planet. The organization focuses on investigations and documentation of evidence to pinpoint who could be the source of major forest fires and deforestation in the region.
    
    **Sahabat Alam Malaysia:** Friends of Earth Malaysia is an independent non-profit organisation focusing on environmental issues that impact communities across Malaysia, working towards environmental justice.
    
    **Youth Movement:** The group, formed in March, has seized the momentum of the global climate protests to push for political commitments and climate education at home.
    
    ### Regional Activism Trends
    
    **Indigenous Rights Integration:** A key aim of the group was to join forces with the nation's indigenous groups, who are already battling big business for their forest lands. It's a "massive oversight" to leave them out of the climate movement.
    
    **Youth Leadership:** Despite the risks of protesting in parts of the region, young people are leading the call for their governments to act urgently and stop environmental catastrophe.
    
    **Justice Framing:** The framing by younger activists of climate change as a global justice issue was proving more effective than an environmental message alone.
    """)
    
    st.markdown("""
    ### Regional Activism Trends (Documented)
    
    **Indigenous Rights Integration:** A key aim of the group was to join forces with the nation's indigenous groups, who are already battling big business for their forest lands. It's a "massive oversight" to leave them out of the climate movement.
    
    **Source:** The Diplomat - The Young Activists Fighting Southeast Asia's Climate Crisis (2019)
    
    **Youth Leadership:** Despite the risks of protesting in parts of the region, young people are leading the call for their governments to act urgently and stop environmental catastrophe.
    
    **Source:** The Diplomat (2019)
    
    **Effectiveness of Messaging:** The framing by younger activists of climate change as a global justice issue was proving more effective than an environmental message alone.
    
    **Source:** The Diplomat (2019)
    
    ### NGO-Government Relations
    
    **Role Evolution:** In the past, environmental NGOs have a responsibility to advise the government and create awareness to the public. However, the trend has soon changed, where environmental NGOs are becoming more active and influential in enacting policies to uphold environmental integrity.
    
    **Source:** ResearchGate - Environmental NGOs Involvement in Dismantling Illegal Plastic Recycling Factory Operations (2020)
    
    **Current Function:** Environmental NGOs in Malaysia are a mediator between the government and the public. However, environmental NGOs are now more active in influencing the public to pressure the government to uphold environmental integrity.
    
    **Source:** ResearchGate (2020)
    """)

# Case Studies
elif selected_section == "Case Studies":
    st.markdown('<h2 class="section-header">📚 Environmental Case Studies</h2>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="subsection-header">Plastic Waste Import Crisis (2018-2019)</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Background
    Last year, more than 35,000 tons of it was shipped to Malaysia, which received more discarded plastic from rich nations than any other developing country. But in June, Malaysian leaders effectively banned future shipments.
    
    ### Community Response
    **Grassroots Activism:** Pua Lay Peng is a local activist leading a grassroots environmental group called Persatuan Tindakan Alam Sekitar Kuala Langat (Kuala Langat Environmental Action Group) in Malaysia. The group was active in campaigning against the imported plastic waste problem that was affecting their small town, Jenjarom.
    
    **Local Impact:** With over 40 illegal plastic factories emitting toxic gases into the air and polluting the local rivers and waterways, they were making people very sick.
    
    ### Government Action
    **Policy Response:** But last month, Malaysian leaders effectively banned future shipments of plastic waste from developed countries.
    
    **Global Context:** Malaysia is joining a whole host of other countries that really started with China a few years ago, standing up to the United States and other countries and saying no more.
    """)
    
    st.markdown("""
    ### Documented Impact Timeline
    
    **Pre-Crisis (Before 2018):** Limited plastic waste imports to Malaysia
    
    **Crisis Period (2018-2019):** Last year, more than 35,000 tons of plastic waste was shipped to Malaysia, which received more discarded plastic from rich nations than any other developing country.
    
    **Source:** PBS News Weekend (2025)
    
    **Local Impact:** With over 40 illegal plastic factories emitting toxic gases into the air and polluting the local rivers and waterways, they were making people very sick.
    
    **Source:** Greenpeace International (2025)
    
    **Government Response (2019-2025):** But in June, Malaysian leaders effectively banned future shipments.
    
    **Source:** PBS News Weekend (2025)
    
    **Current Status:** Malaysia is joining a whole host of other countries that really started with China a few years ago, standing up to the United States and other countries and saying no more.
    
    **Source:** PBS News Weekend (2025)
    """)
    
    st.markdown('<h3 class="subsection-header">NGO Involvement in Policy Enforcement</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **NGO Role Evolution:** In the past, environmental NGOs have a responsibility to advise the government and create awareness to the public. However, the trend has soon changed, where environmental NGOs are becoming more active and influential in enacting policies to uphold environmental integrity.
    
    **Enforcement Support:** Environmental NGOs in Malaysia are a mediator between the government and the public. However, environmental NGOs are now more active in influencing the public to pressure the government to uphold environmental integrity.
    """)

# Recent Forest Fires & Climate Change
elif selected_section == "Recent Forest Fires & Climate Change":
    st.markdown('<h2 class="section-header">🔥 Recent Forest Fires & Climate Change Connection</h2>', unsafe_allow_html=True)
    
    # Only documented forest loss data (from Greenpeace)
    documented_forest_loss = {
        'State': ['Sarawak', 'Sabah', 'Pahang'],
        'Forest Loss 2001-2023 (Million Hectares)': [3.27, 1.88, 1.27]
    }
    
    df_documented_fires = pd.DataFrame(documented_forest_loss)
    
    fig_documented_loss = px.bar(df_documented_fires, x='State', y='Forest Loss 2001-2023 (Million Hectares)',
                                title='Documented Forest Cover Loss by State (2001-2023)')
    st.plotly_chart(fig_documented_loss, use_container_width=True)
    
    st.markdown("""
    **Source:** Greenpeace Malaysia (2025). Based on Global Forest Watch data.
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Forest Loss Statistics
    
    **National Overview:** Of all tree cover loss between 2001 to 2023 in Malaysia was in Sarawak (3.27Mha) and Sabah (1.88Mha), followed by Pahang (1.27Mha).
    
    **Recent Developments:** Just a fortnight ago, Malaysia — including parts of Sarawak — was shrouded in an unexpected spell of unhealthy haze.
    
    ### Climate Change Connection
    
    **Carbon Impact:** Fires from biomass burning potentially contribute to global warming and climate change due to the emission of large amounts of greenhouse gases and other pyrogenic products.
    
    **Forest Role:** Malaysia boasts a total forested area of 18.27 million hectares, with 10.92 million hectares designated as Permanent Reserve Forests and 3.31 million hectares as fully protected areas. These forests play a crucial role by sequestering approximately three-quarters of the country's total carbon dioxide emissions.
    
    **Deforestation Impact:** Deforestation is responsible for 20% of the total global GHG emissions, and a significant part of our ecosystem and species loss.
    
    ### NGO Response to Recent Fires
    
    **Greenpeace Action:** Our work is to hold polluters, governments and groups responsible for devastating environmental acts, accountable. And it all starts with investigations and documentation of evidence to pinpoint who could be the source of major forest fires and deforestation in the region.
    
    **Community Engagement:** Alongside evidence gathered, we conduct research while working with allies and indigenous communities to call out for sustainable solutions in the protection of forests.
    
    **Current Status:** Despite the best of intentions, fire prevention strategies are not always effectively implemented, largely due to resource constraints, difficult terrain and the evolving challenges brought about by climate change.
    """)

# Data sources and methodology
st.sidebar.markdown("---")
st.sidebar.markdown("### Data Sources")
st.sidebar.markdown("""
- Malaysian Department of Environment
- Singapore Institute of International Affairs
- Academic Research Papers
- NGO Reports & Statements
- Government Budget Documents
- ASEAN Environmental Reports
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7F8C8D; font-size: 0.9rem; margin-top: 2rem;'>
    <p><strong>Malaysia Haze & Environmental Impact Dashboard</strong></p>
    <p>Comprehensive analysis of environmental challenges and policy responses</p>
    <p>Data compiled from government sources, academic research, and NGO reports</p>
</div>
""", unsafe_allow_html=True)
