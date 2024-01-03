template = [
    {
        "header": "title",
        "display_name": "Project Title",
        "word_limit": 20,
        "type": "plain_text",
        "default_prompt": "write title for the proposal",
        "graph": None,
        "graph_type": None
    },
    {
        "header": "proposedBy",
        "display_name": "Proposed By",
        "word_limit": 10,
        "type": "plain_text",
        "default_prompt": "write proposed by for the proposal. Make it precious. avoid giving any preemptive and write the answer directly",
        "graph": False,
    },
    {
        "header": "introduction",
        "display_name": "Introduction",
        "word_limit": 200,
        "type": "plain_text",
        "default_prompt": "write introduction for the proposal. Make it clear and professional. avoid giving any preemptive and write the answer directly",
        "graph": None,
        "graph_type": None
    },
    {
        "header": "objectives",
        "display_name": "Objective",
        "word_limit": 150,
        "type": "plain_text",
        "default_prompt": "write objectives for the proposal. avoid giving any preemptive and write the answer directly. if you point them out, then do not forget to give line break to ensure that each point is in a separeate line",
        "graph": None,
        "graph_type": None
    }
    ,
    # {
    #     "header": "address",
    #     "display_name": "Address",
    #     "word_limit": 50,
    #     "type": "plain_text",
    #     "default_prompt": "User will give office address",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "phoneNumber",
    #     "display_name": "Phone Number",
    #     "word_limit": 20,
    #     "type": "plain_text",
    #     "default_prompt": "User will give phone number",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "email",
    #     "display_name": "Email",
    #     "word_limit": 30,
    #     "type": "plain_text",
    #     "default_prompt": "User will give email",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "website",
    #     "display_name": "Website",
    #     "word_limit": 30,
    #     "type": "plain_text",
    #     "default_prompt": "User will give website link",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "referenceNumber",
    #     "display_name": "Reference Number",
    #     "word_limit": 20,
    #     "type": "plain_text",
    #     "default_prompt": "User will give reference number",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "submissionDate",
    #     "display_name": "Date of Submission",
    #     "word_limit": 15,
    #     "type": "plain_text",
    #     "default_prompt": "User will give submission date",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "backgroundAndExperience",
    #     "display_name": "Background and Experience",
    #     "word_limit": 250,
    #     "type": "plain_text",
    #     "default_prompt": "User will give company background and experience",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "whyChooseUs",
    #     "display_name": "Why Choose Us",
    #     "word_limit": 150,
    #     "type": "plain_text",
    #     "default_prompt": "Generate compelling content that highlights the key reasons why users should choose a product or service. Cover aspects such as unique features, benefits, and any competitive advantages. Ensure the content is persuasive and informative to encourage user trust and engagement.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "clientRequirements",
    #     "display_name": "Client Requirements",
    #     "word_limit": 200,
    #     "type": "plain_text",
    #     "default_prompt": "User will give client requirements.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "uniqueSellingProposition",
    #     "display_name": "Unique Selling Proposition",
    #     "word_limit": 100,
    #     "type": "plain_text",
    #     "default_prompt": "Generate a unique selling proposition for a product or service.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "scopeOfWork",
    #     "display_name": "Scope Of Work",
    #     "word_limit": 250,
    #     "type": "plain_text",
    #     "default_prompt": "Generate a detailed and comprehensive description of the scope of work under the header scopeOfWork. Include key tasks, milestones, and any specific requirements or considerations.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "projectTeam",
    #     "display_name": "Project Team",
    #     "word_limit": 150,
    #     "type": "plain_text",
    #     "default_prompt": "User will generate information or details about a project team ",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "projectSchedule",
    #     "display_name": "Project Schedule",
    #     "word_limit": 100,
    #     "type": "plain_text",
    #     "default_prompt": "User will give details about project Schedule",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "estimatedProjectCost",
    #     "display_name": "Estimated Project Cost",
    #     "word_limit": 100,
    #     "type": "plain_text",
    #     "default_prompt": "User will give details about estimated project cost ",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "breakdownOfCosts",
    #     "display_name": "Breakdown Of Costs",
    #     "word_limit": 200,
    #     "type": "plain_text",
    #     "default_prompt": "User will give details of breakdown of costs.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "termsAndConditions",
    #     "display_name": "Terms And Conditions",
    #     "word_limit": 250,
    #     "type": "plain_text",
    #     "default_prompt": "Write the Terms And Conditions section for the project proposal. Clearly define the terms and conditions governing the project, including responsibilities, deliverables, timelines, and any relevant contractual details. Ensure precision and completeness in outlining the terms and conditions for a comprehensive understanding.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "systemSpecifications",
    #     "display_name": "System Specifications",
    #     "word_limit": 200,
    #     "type": "plain_text",
    #     "default_prompt": "Write the System Specifications section for the project proposal. Detail the technical specifications of the system, including hardware, software, and network requirements. Be thorough in outlining the specifications to provide a comprehensive overview of the project's technological needs.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "hardwareSpecifications",
    #     "display_name": "Hardware Specifications",
    #     "word_limit": 150,
    #     "type": "plain_text",
    #     "default_prompt": "Develop the Hardware Specifications section for the project proposal. Provide detailed information on the required hardware components, configurations, and any specific standards. Ensure clarity and completeness in outlining the hardware specifications for a comprehensive understanding of the project's infrastructure needs.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "proposedSolutionArchitecture",
    #     "display_name": "Proposed Solution Architecture",
    #     "word_limit": 200,
    #     "type": "plain_text",
    #     "default_prompt": "Write the Proposed Solution Architecture section for the project proposal. Outline the architectural design of the proposed solution, including key components, system interactions, and integration points. Ensure clarity and completeness in presenting the solution architecture for a comprehensive understanding.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "serviceDeliveryPolicies",
    #     "display_name": "Service Delivery Policies",
    #     "word_limit": 150,
    #     "type": "plain_text",
    #     "default_prompt": "Compose the service delivery policies section for the project proposal. Outline the policies governing service delivery, including timelines, procedures, and any relevant guidelines. Ensure clarity and coherence in presenting the delivery policies for a comprehensive understanding.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "testingAndQualityAssurance",
    #     "display_name": "Testing And QualityAssurance",
    #     "word_limit": 150,
    #     "type": "plain_text",
    #     "default_prompt": "Write the testing and quality assurance segment for the project proposal. Detail the testing methodologies, quality assurance processes, and criteria for success. Include measures to ensure the project meets established standards. Keep it clear and incorporate any relevant industry best practices.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "serviceWarrantyAndSupport",
    #     "display_name": "Service Warranty And Support",
    #     "word_limit": 150,
    #     "type": "plain_text",
    #     "default_prompt": "Write the service warranty and support section for the project proposal. Specify the service warranty terms and outline the support framework. Include details on how issues will be addressed and resolved. Keep this section concise yet informative.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "liability",
    #     "display_name": "Liability",
    #     "word_limit": 100,
    #     "type": "plain_text",
    #     "default_prompt": "Write a comprehensive liability section in the project proposal. Clearly outline potential liabilities, risk mitigation measures, and responsibilities. Ensure this section is thorough and aligned with project objectives.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "benefitsAndOutcomes",
    #     "display_name": "Benefits And Outcomes",
    #     "word_limit": 200,
    #     "type": "plain_text",
    #     "default_prompt": "Please write the benefitsAndOutcomes section for the project proposal. Be sure to outline the anticipated benefits and outcomes, including measurable results. Keep this section focused and include any key points supporting the project's success.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "riskAssessment",
    #     "display_name": "Risk Assessment",
    #     "word_limit": 150,
    #     "type": "plain_text",
    #     "default_prompt": "Please write the risk assessment for this project proposal. Ensure to include potential risks. Keep it concise yet comprehensive.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "references",
    #     "display_name": "References",
    #     "word_limit": 200,  
    #     "type": "plain_text",
    #     "default_prompt": "Write some references and client reviews to enhance the efficiency, so that it creates a positive impact on the project proposal",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "ethicalConsideration",
    #     "display_name": "Ethical Consideration",
    #     "word_limit": 150,
    #     "type": "plain_text",
    #     "default_prompt": "This project is in compliance with proper rules, regulation and concent from employees. There is nothing unethical in it. This will be both legal and ethical. So write the Ethical Consideration portion of this project in the proposal.",
    #     "graph": None,
    #     "graph_type": None
    # },
    # {
    #     "header": "conclusion",
    #     "display_name": "Conclusion",
    #     "word_limit": 100,
    #     "type": "plain_text",
    #     "default_prompt": "Write a proper and formal conclusion for the project, summarizing all the important and key points",
    #     "graph": None,
    #     "graph_type": None
    # }
]