"""Product-authored information-flow relationships between CSF 2.0 outcomes.

The CSF Core defines outcomes, not a required implementation order.  This
catalog records a deliberately limited set of planning relationships for the
product: information an outcome can make available and downstream outcomes
that use that information.  It is not an official NIST dependency map and it
does not require a user to implement a particular control or follow one fixed
sequence.
"""

from typing import Dict, List


INFORMATION_ITEMS: List[Dict[str, str]] = [
    {
        "information_id": "organizational_mission",
        "title": "Organizational mission and objectives",
        "description": "What the organization is trying to accomplish and which objectives cybersecurity decisions must support.",
    },
    {
        "information_id": "stakeholder_cybersecurity_needs",
        "title": "Stakeholder cybersecurity and privacy needs",
        "description": "The needs and expectations of people and organizations affected by cybersecurity decisions.",
    },
    {
        "information_id": "legal_contractual_requirements",
        "title": "Legal, regulatory, and contractual requirements",
        "description": "Applicable cybersecurity, privacy, and agreement requirements that constrain decisions and communications.",
    },
    {
        "information_id": "critical_services_and_objectives",
        "title": "Critical services and objectives",
        "description": "Services, capabilities, and objectives that others depend on, including their expected resilience.",
    },
    {
        "information_id": "external_dependencies",
        "title": "External dependencies",
        "description": "External products, services, facilities, and providers needed to support important work.",
    },
    {
        "information_id": "risk_objectives_and_tolerance",
        "title": "Risk objectives, tolerance, and response direction",
        "description": "The organization's agreed objectives, acceptable risk boundaries, and response options.",
    },
    {
        "information_id": "risk_assessment_method",
        "title": "Risk assessment method",
        "description": "The common method used to calculate, document, categorize, and prioritize cybersecurity risk.",
    },
    {
        "information_id": "cybersecurity_roles",
        "title": "Cybersecurity roles and authorities",
        "description": "Who is responsible for decisions, implementation, review, escalation, and communication.",
    },
    {
        "information_id": "supplier_criticality",
        "title": "Supplier criticality and priority",
        "description": "Which suppliers and providers are important enough to require deeper review, requirements, or monitoring.",
    },
    {
        "information_id": "asset_inventory",
        "title": "Asset inventory",
        "description": "Known hardware, software, systems, services, and data managed by the organization.",
    },
    {
        "information_id": "network_and_data_flows",
        "title": "Network communication and data flows",
        "description": "How authorized systems communicate and where information moves internally and externally.",
    },
    {
        "information_id": "asset_criticality",
        "title": "Asset criticality and impact",
        "description": "The relative importance of assets based on mission, resources, classification, and likely impact.",
    },
    {
        "information_id": "vulnerabilities_and_threats",
        "title": "Validated vulnerabilities and relevant threats",
        "description": "Known weaknesses and internal or external threats that could affect the organization.",
    },
    {
        "information_id": "risk_scenarios_and_priorities",
        "title": "Risk scenarios and priorities",
        "description": "Recorded likelihoods, impacts, inherent risk, and the order in which risks should be addressed.",
    },
    {
        "information_id": "selected_risk_responses",
        "title": "Selected risk responses",
        "description": "Chosen, planned, tracked, and communicated actions for addressing prioritized risk.",
    },
    {
        "information_id": "change_and_exception_risk_records",
        "title": "Change and exception risk records",
        "description": "Documented risk impacts, approvals, exceptions, planned responses, and tracking information for proposed changes and exceptions.",
    },
    {
        "information_id": "secure_development_performance_results",
        "title": "Secure development performance results",
        "description": "Recorded results from monitoring secure software development practices throughout the software development life cycle.",
    },
    {
        "information_id": "authorized_adverse_event_alerts",
        "title": "Authorized adverse-event alerts",
        "description": "Adverse-event alerts, log-analysis findings, and tickets delivered to authorized staff and tools for review and response.",
    },
    {
        "information_id": "monitoring_findings",
        "title": "Monitoring findings and potentially adverse events",
        "description": "Signals from monitored environments, systems, providers, and personnel activity that need analysis.",
    },
    {
        "information_id": "incident_analysis",
        "title": "Incident analysis and response status",
        "description": "What happened, its scope and impact, the investigation record, and the current response status.",
    },
    {
        "information_id": "recovery_priorities_and_status",
        "title": "Recovery priorities and restoration status",
        "description": "What must be restored first, the integrity checks required, and progress toward normal operation.",
    },
    {
        "information_id": "improvement_lessons",
        "title": "Lessons and improvement opportunities",
        "description": "Findings from evaluations, exercises, operations, incidents, and recovery that should improve future work.",
    },
    {
        "information_id": "supplier_requirements_and_agreements",
        "title": "Supplier requirements and agreements",
        "description": "Documented cybersecurity requirements, responsibilities, and agreement terms for suppliers and other third parties.",
    },
    {
        "information_id": "supply_chain_program_direction",
        "title": "Supply-chain program direction",
        "description": "The agreed supply-chain risk strategy, objectives, policies, and processes that guide supplier work.",
    },
    {
        "information_id": "supplier_lifecycle_results",
        "title": "Supplier lifecycle results",
        "description": "Recorded supplier risk, assessment, response, and monitoring results over the relationship lifecycle.",
    },
    {
        "information_id": "threat_intelligence",
        "title": "Threat intelligence",
        "description": "Relevant internal and external threat information received from sharing forums and other sources.",
    },
    {
        "information_id": "restoration_assets",
        "title": "Restoration assets",
        "description": "Backups and other assets maintained for restoring systems, services, and data.",
    },
    {
        "information_id": "verified_restoration_assets",
        "title": "Verified restoration assets",
        "description": "Backups and restoration assets whose integrity has been checked before restoration use.",
    },
    {
        "information_id": "log_records",
        "title": "Log records",
        "description": "Generated logs that support continuous monitoring, investigation, and evidence preservation.",
    },
    {
        "information_id": "event_threat_context",
        "title": "Event threat context",
        "description": "Threat intelligence and contextual information applied when analyzing potentially adverse events.",
    },
    {
        "information_id": "analyzed_event_information",
        "title": "Analyzed event information",
        "description": "Analyzed potentially adverse events, including the associated activity, impact, scope, and incident decision.",
    },
    {
        "information_id": "triaged_incident_reports",
        "title": "Triaged incident reports",
        "description": "Incident reports that have been received, validated, and prepared for categorization and prioritization.",
    },
    {
        "information_id": "incident_priority_and_scope",
        "title": "Incident priority and scope",
        "description": "The categorized incident priority and validated magnitude, scope, and impact needed for escalation or recovery decisions.",
    },
    {
        "information_id": "recovery_initiation_decision",
        "title": "Recovery initiation decision",
        "description": "The decision and criteria that initiate the recovery portion of the incident response process.",
    },
    {
        "information_id": "preserved_investigation_records",
        "title": "Preserved investigation records",
        "description": "Investigation actions and records whose integrity and provenance have been preserved.",
    },
    {
        "information_id": "external_vulnerability_disclosures",
        "title": "External vulnerability disclosures",
        "description": "Vulnerability reports received from external reporters, vendors, researchers, or disclosure channels.",
    },
    {
        "information_id": "incident_response_plan",
        "title": "Incident response plan",
        "description": "The plan and coordination arrangements used to respond to a declared incident with relevant third parties.",
    },
    {
        "information_id": "risk_management_measures_and_results",
        "title": "Risk-management measures and thresholds",
        "description": "The agreed KPIs, KRIs, and thresholds used to judge cybersecurity risk-management performance.",
    },
    {
        "information_id": "external_legal_contractual_sources",
        "title": "External legal, regulatory, and contractual sources",
        "description": "Applicable laws, regulations, contracts, privacy obligations, and other external requirements that the organization must identify and manage.",
    },
    {
        "information_id": "risk_management_performance_results",
        "title": "Risk-management performance results",
        "description": "Actual measurements, assessment results, monitoring findings, action status, supplier results, and incident results used to evaluate cybersecurity risk management.",
    },
    {
        "information_id": "risk_management_review_findings",
        "title": "Risk-management review findings",
        "description": "Performance-review findings and recommended adjustments to cybersecurity risk-management strategy, direction, or policy.",
    },
    {
        "information_id": "integrated_supply_chain_risk_records",
        "title": "Integrated supply-chain risk records",
        "description": "Material supplier and supply-chain risk information, including integrated control considerations, prepared for enterprise risk management.",
    },
]


# An outcome may be a source, but the same information can also come from
# equivalent existing records or a custom action.  ``source_guidance`` keeps
# that flexibility explicit for future UI and workflow work.
INFORMATION_SOURCES: List[Dict[str, str]] = [
    {"information_id": "organizational_mission", "source_subcategory_id": "GV.OC-01", "source_guidance": "A current mission statement, service strategy, or equivalent record may provide this information."},
    {"information_id": "stakeholder_cybersecurity_needs", "source_subcategory_id": "GV.OC-02", "source_guidance": "A stakeholder record, consultation, existing policy record, or custom action may provide this information."},
    {"information_id": "legal_contractual_requirements", "source_subcategory_id": "GV.OC-03", "source_guidance": "A legal, privacy, contractual, or compliance record may provide this information."},
    {"information_id": "critical_services_and_objectives", "source_subcategory_id": "GV.OC-04", "source_guidance": "A business-impact, service-level, or continuity record may provide this information."},
    {"information_id": "external_dependencies", "source_subcategory_id": "GV.OC-05", "source_guidance": "A supplier, service, facility, or dependency inventory may provide this information."},
    {"information_id": "risk_objectives_and_tolerance", "source_subcategory_id": "GV.RM-01", "source_guidance": "Risk objectives may be combined with tolerance and response-direction records."},
    {"information_id": "risk_objectives_and_tolerance", "source_subcategory_id": "GV.RM-02", "source_guidance": "Risk tolerance may be combined with objectives and response-direction records."},
    {"information_id": "risk_objectives_and_tolerance", "source_subcategory_id": "GV.RM-04", "source_guidance": "Risk response direction may be combined with objectives and tolerance records."},
    {"information_id": "risk_assessment_method", "source_subcategory_id": "GV.RM-06", "source_guidance": "An established risk assessment method or equivalent documented process may provide this information."},
    {"information_id": "cybersecurity_roles", "source_subcategory_id": "GV.RR-02", "source_guidance": "A responsibility assignment, policy, or owner record may provide this information."},
    {"information_id": "supplier_criticality", "source_subcategory_id": "GV.SC-04", "source_guidance": "A supplier inventory, criticality assessment, or dependency record may provide this information."},
    {"information_id": "asset_inventory", "source_subcategory_id": "ID.AM-01", "source_guidance": "A managed hardware inventory may provide this information."},
    {"information_id": "asset_inventory", "source_subcategory_id": "ID.AM-02", "source_guidance": "A managed software, service, or system inventory may provide this information."},
    {"information_id": "asset_inventory", "source_subcategory_id": "ID.AM-04", "source_guidance": "A supplier-service inventory may provide this information."},
    {"information_id": "asset_inventory", "source_subcategory_id": "ID.AM-07", "source_guidance": "A designated-data inventory may provide this information."},
    {"information_id": "network_and_data_flows", "source_subcategory_id": "ID.AM-03", "source_guidance": "A current network diagram, authorized communication record, or data-flow record may provide this information."},
    {"information_id": "asset_criticality", "source_subcategory_id": "ID.AM-05", "source_guidance": "An asset classification, business-impact, or mission-impact record may provide this information."},
    {"information_id": "vulnerabilities_and_threats", "source_subcategory_id": "ID.RA-01", "source_guidance": "Validated vulnerability records may provide this information."},
    {"information_id": "vulnerabilities_and_threats", "source_subcategory_id": "ID.RA-03", "source_guidance": "Threat records or current threat intelligence may provide this information."},
    {"information_id": "risk_scenarios_and_priorities", "source_subcategory_id": "ID.RA-04", "source_guidance": "Recorded likelihood and impact analysis may provide this information."},
    {"information_id": "risk_scenarios_and_priorities", "source_subcategory_id": "ID.RA-05", "source_guidance": "A risk register or prioritization record may provide this information."},
    {"information_id": "selected_risk_responses", "source_subcategory_id": "ID.RA-06", "source_guidance": "A recorded treatment decision, action plan, or accepted-risk record may provide this information."},
    {"information_id": "change_and_exception_risk_records", "source_subcategory_id": "ID.RA-07", "source_guidance": "Documented change and exception reviews, approvals, risk impacts, and tracking records may provide this information."},
    {"information_id": "secure_development_performance_results", "source_subcategory_id": "PR.PS-06", "source_guidance": "Monitoring records for secure software development practices throughout the life cycle may provide this information."},
    {"information_id": "authorized_adverse_event_alerts", "source_subcategory_id": "DE.AE-06", "source_guidance": "Authorized staff and tools may receive adverse-event alerts, log-analysis findings, and tickets through this distribution process."},
    {"information_id": "monitoring_findings", "source_subcategory_id": "DE.CM-01", "source_guidance": "Monitoring records may provide this information."},
    {"information_id": "monitoring_findings", "source_subcategory_id": "DE.CM-03", "source_guidance": "Personnel activity and technology-usage monitoring may provide this information."},
    {"information_id": "monitoring_findings", "source_subcategory_id": "DE.CM-06", "source_guidance": "External-provider monitoring may provide this information."},
    {"information_id": "monitoring_findings", "source_subcategory_id": "DE.CM-09", "source_guidance": "Hardware, software, runtime, and data monitoring may provide this information."},
    {"information_id": "incident_analysis", "source_subcategory_id": "DE.AE-08", "source_guidance": "An incident declaration and related analysis records may provide this information."},
    {"information_id": "incident_analysis", "source_subcategory_id": "RS.AN-03", "source_guidance": "Incident investigation and root-cause analysis may provide this information."},
    {"information_id": "incident_analysis", "source_subcategory_id": "RS.AN-08", "source_guidance": "Incident magnitude and scope analysis may provide this information."},
    {"information_id": "recovery_priorities_and_status", "source_subcategory_id": "RC.RP-02", "source_guidance": "Recovery action selection and progress records may provide this information."},
    {"information_id": "recovery_priorities_and_status", "source_subcategory_id": "RC.RP-05", "source_guidance": "Restoration verification and normal-operation confirmation may provide this information."},
    {"information_id": "improvement_lessons", "source_subcategory_id": "ID.IM-01", "source_guidance": "Evaluation findings may provide this information."},
    {"information_id": "improvement_lessons", "source_subcategory_id": "ID.IM-02", "source_guidance": "Test and exercise findings may provide this information."},
    {"information_id": "improvement_lessons", "source_subcategory_id": "ID.IM-03", "source_guidance": "Operational and incident lessons may provide this information."},
    {"information_id": "supplier_requirements_and_agreements", "source_subcategory_id": "GV.SC-05", "source_guidance": "Supplier cybersecurity requirements, contracts, and equivalent agreement records may provide this information."},
    {"information_id": "supply_chain_program_direction", "source_subcategory_id": "GV.SC-01", "source_guidance": "The approved supply-chain risk management program or equivalent strategy record may provide this information."},
    {"information_id": "supplier_lifecycle_results", "source_subcategory_id": "GV.SC-07", "source_guidance": "Supplier risk, assessment, response, and monitoring records may provide this information."},
    {"information_id": "threat_intelligence", "source_subcategory_id": "ID.RA-02", "source_guidance": "Threat intelligence received from sharing forums and other sources may provide this information."},
    {"information_id": "restoration_assets", "source_subcategory_id": "PR.DS-11", "source_guidance": "Maintained backups and other restoration assets may provide this information."},
    {"information_id": "verified_restoration_assets", "source_subcategory_id": "RC.RP-03", "source_guidance": "Verified backups and restoration assets may provide this information."},
    {"information_id": "log_records", "source_subcategory_id": "PR.PS-04", "source_guidance": "Generated log records may provide this information."},
    {"information_id": "event_threat_context", "source_subcategory_id": "DE.AE-07", "source_guidance": "Threat intelligence and other contextual information integrated into analysis may provide this information."},
    {"information_id": "analyzed_event_information", "source_subcategory_id": "DE.AE-02", "source_guidance": "Analysis of potentially adverse events may provide this information."},
    {"information_id": "analyzed_event_information", "source_subcategory_id": "DE.AE-04", "source_guidance": "Estimated event impact and scope may provide this information."},
    {"information_id": "analyzed_event_information", "source_subcategory_id": "DE.AE-08", "source_guidance": "An incident declaration and its supporting analysis may provide this information."},
    {"information_id": "triaged_incident_reports", "source_subcategory_id": "RS.MA-02", "source_guidance": "Validated and triaged incident reports may provide this information."},
    {"information_id": "incident_priority_and_scope", "source_subcategory_id": "RS.MA-03", "source_guidance": "Categorized and prioritized incident records may provide this information."},
    {"information_id": "incident_priority_and_scope", "source_subcategory_id": "RS.AN-08", "source_guidance": "Validated incident magnitude and scope analysis may provide this information."},
    {"information_id": "recovery_initiation_decision", "source_subcategory_id": "RS.MA-05", "source_guidance": "The applied recovery-initiation criteria and decision may provide this information."},
    {"information_id": "preserved_investigation_records", "source_subcategory_id": "RS.AN-06", "source_guidance": "Recorded investigation actions with preserved integrity and provenance may provide this information."},
    {"information_id": "external_vulnerability_disclosures", "source_subcategory_id": "External: vulnerability disclosure sources", "source_guidance": "External reporters, vendors, researchers, and disclosure channels may provide this information."},
    {"information_id": "incident_response_plan", "source_subcategory_id": "RS.MA-01", "source_guidance": "The executed incident response plan and its third-party coordination arrangements may provide this information."},
    {"information_id": "cybersecurity_roles", "source_subcategory_id": "GV.SC-02", "source_guidance": "Coordinated supplier, customer, partner, and internal cybersecurity responsibilities may provide this information."},
    {"information_id": "risk_management_measures_and_results", "source_subcategory_id": "GV.RM-01", "source_guidance": "Risk-management objectives can define the KPIs, KRIs, and thresholds used to judge whether those objectives are being achieved."},
    {"information_id": "external_legal_contractual_sources", "source_subcategory_id": "External: legal, regulatory, and contractual sources", "source_guidance": "Applicable laws, regulations, contracts, privacy obligations, and other authoritative external sources may provide this information."},
    {"information_id": "risk_management_performance_results", "source_subcategory_id": "External: operational measurement and evidence records", "source_guidance": "Monitoring, assessment, action, supplier, incident, and other operational records may provide these measured results."},
    {"information_id": "risk_management_review_findings", "source_subcategory_id": "GV.OV-03", "source_guidance": "Performance evaluation and review records may provide these findings and recommended adjustments."},
    {"information_id": "integrated_supply_chain_risk_records", "source_subcategory_id": "GV.SC-03", "source_guidance": "Integrated supply-chain risk records, material-risk escalations, and control-set considerations may provide this information."},
    {"information_id": "vulnerabilities_and_threats", "source_subcategory_id": "ID.RA-08", "source_guidance": "Validated vulnerability disclosures may provide this information."},
    {"information_id": "incident_analysis", "source_subcategory_id": "RS.AN-06", "source_guidance": "Preserved investigation records may provide this information."},
    {"information_id": "incident_analysis", "source_subcategory_id": "RS.AN-07", "source_guidance": "Collected and preserved incident data may provide this information."},
]


# ``required_input`` means that this information should be available before a
# user represents the downstream activity as complete.  ``planning_input``
# means it should be considered but an equivalent source or documented reason
# may be sufficient. ``event_input`` becomes relevant when the downstream
# incident or recovery work has been triggered.
INFORMATION_USES: List[Dict[str, str]] = [
    {"information_id": "organizational_mission", "consumer_subcategory_id": "GV.RM-01", "dependency_kind": "planning_input", "use_reason": "Set risk-management objectives that support what the organization is trying to accomplish."},
    {"information_id": "organizational_mission", "consumer_subcategory_id": "ID.AM-05", "dependency_kind": "planning_input", "use_reason": "Prioritize assets according to their effect on mission objectives."},
    {"information_id": "organizational_mission", "consumer_subcategory_id": "ID.RA-04", "dependency_kind": "planning_input", "use_reason": "Estimate impact in terms of the mission and objectives that could be affected."},
    {"information_id": "organizational_mission", "consumer_subcategory_id": "RC.RP-04", "dependency_kind": "planning_input", "use_reason": "Establish post-incident operating priorities using critical mission functions."},

    {"information_id": "stakeholder_cybersecurity_needs", "consumer_subcategory_id": "GV.RM-01", "dependency_kind": "planning_input", "use_reason": "Agree risk-management objectives that account for affected stakeholders' needs and expectations."},
    {"information_id": "stakeholder_cybersecurity_needs", "consumer_subcategory_id": "GV.RM-05", "dependency_kind": "planning_input", "use_reason": "Set communication paths that reach people who need cybersecurity risk information."},
    {"information_id": "stakeholder_cybersecurity_needs", "consumer_subcategory_id": "GV.SC-01", "dependency_kind": "planning_input", "use_reason": "Set supply-chain objectives and processes that account for relevant stakeholder needs."},
    {"information_id": "stakeholder_cybersecurity_needs", "consumer_subcategory_id": "GV.SC-05", "dependency_kind": "required_input", "use_reason": "Translate known security and privacy needs into supplier and purchasing requirements."},
    {"information_id": "stakeholder_cybersecurity_needs", "consumer_subcategory_id": "RS.CO-02", "dependency_kind": "planning_input", "use_reason": "Determine which internal and external stakeholders must be notified of an incident and what they need to know."},
    {"information_id": "stakeholder_cybersecurity_needs", "consumer_subcategory_id": "RS.CO-03", "dependency_kind": "planning_input", "use_reason": "Share incident information in a way that accounts for designated stakeholders' needs and expectations."},
    {"information_id": "stakeholder_cybersecurity_needs", "consumer_subcategory_id": "RC.CO-03", "dependency_kind": "planning_input", "use_reason": "Communicate recovery progress to stakeholders who rely on the affected capabilities or information."},

    {"information_id": "legal_contractual_requirements", "consumer_subcategory_id": "GV.PO-01", "dependency_kind": "planning_input", "use_reason": "Establish policy that reflects applicable legal, regulatory, and contractual obligations."},
    {"information_id": "legal_contractual_requirements", "consumer_subcategory_id": "GV.PO-02", "dependency_kind": "planning_input", "use_reason": "Update policy when applicable requirements change."},
    {"information_id": "legal_contractual_requirements", "consumer_subcategory_id": "GV.SC-05", "dependency_kind": "required_input", "use_reason": "Include applicable security, privacy, and contractual obligations in supplier requirements and agreements."},
    {"information_id": "legal_contractual_requirements", "consumer_subcategory_id": "RS.CO-02", "dependency_kind": "planning_input", "use_reason": "Determine notification duties and deadlines during incident response."},
    {"information_id": "legal_contractual_requirements", "consumer_subcategory_id": "RC.CO-04", "dependency_kind": "planning_input", "use_reason": "Use approved methods and messaging that meet applicable public-update requirements."},

    {"information_id": "critical_services_and_objectives", "consumer_subcategory_id": "ID.AM-05", "dependency_kind": "planning_input", "use_reason": "Prioritize assets by their importance to services and objectives that others rely on."},
    {"information_id": "critical_services_and_objectives", "consumer_subcategory_id": "ID.RA-04", "dependency_kind": "planning_input", "use_reason": "Estimate the impact of a threat scenario on important services and objectives."},
    {"information_id": "critical_services_and_objectives", "consumer_subcategory_id": "PR.IR-03", "dependency_kind": "planning_input", "use_reason": "Set resilience requirements for normal and adverse situations."},
    {"information_id": "critical_services_and_objectives", "consumer_subcategory_id": "RC.RP-02", "dependency_kind": "required_input", "use_reason": "Select and prioritize recovery actions according to the services and objectives that need restoration."},
    {"information_id": "critical_services_and_objectives", "consumer_subcategory_id": "RC.RP-04", "dependency_kind": "required_input", "use_reason": "Establish post-incident operating norms using critical mission functions and services."},
    {"information_id": "critical_services_and_objectives", "consumer_subcategory_id": "RC.CO-03", "dependency_kind": "planning_input", "use_reason": "Explain recovery progress for capabilities that stakeholders depend on."},

    {"information_id": "external_dependencies", "consumer_subcategory_id": "ID.AM-04", "dependency_kind": "planning_input", "use_reason": "Maintain an inventory of supplier-provided services that the organization depends on."},
    {"information_id": "external_dependencies", "consumer_subcategory_id": "GV.SC-04", "dependency_kind": "planning_input", "use_reason": "Identify and prioritize suppliers by the importance of the dependency they provide."},
    {"information_id": "external_dependencies", "consumer_subcategory_id": "ID.RA-10", "dependency_kind": "planning_input", "use_reason": "Identify which suppliers are critical enough to assess before acquisition."},
    {"information_id": "external_dependencies", "consumer_subcategory_id": "DE.CM-06", "dependency_kind": "planning_input", "use_reason": "Decide which external services and providers need monitoring for potentially adverse events."},
    {"information_id": "external_dependencies", "consumer_subcategory_id": "RC.RP-02", "dependency_kind": "planning_input", "use_reason": "Account for provider and service dependencies when selecting recovery actions."},

    {"information_id": "risk_objectives_and_tolerance", "consumer_subcategory_id": "GV.PO-01", "dependency_kind": "planning_input", "use_reason": "Align cybersecurity policy with agreed risk objectives, tolerance, and response direction."},
    {"information_id": "risk_objectives_and_tolerance", "consumer_subcategory_id": "ID.RA-06", "dependency_kind": "planning_input", "use_reason": "Choose and prioritize risk responses that fit agreed risk direction and tolerance."},
    {"information_id": "risk_objectives_and_tolerance", "consumer_subcategory_id": "GV.RR-03", "dependency_kind": "planning_input", "use_reason": "Allocate resources in line with the cybersecurity risk strategy and priorities."},
    {"information_id": "risk_assessment_method", "consumer_subcategory_id": "ID.RA-04", "dependency_kind": "required_input", "use_reason": "Use the established method to calculate and record likelihood and impact."},
    {"information_id": "risk_assessment_method", "consumer_subcategory_id": "ID.RA-05", "dependency_kind": "required_input", "use_reason": "Use the established method to understand inherent risk and prioritize responses consistently."},
    {"information_id": "risk_assessment_method", "consumer_subcategory_id": "ID.RA-06", "dependency_kind": "planning_input", "use_reason": "Use the established method when selecting, tracking, and communicating risk responses."},
    {"information_id": "risk_assessment_method", "consumer_subcategory_id": "ID.RA-07", "dependency_kind": "required_input", "use_reason": "Use the established method to assess and record the risk impact of proposed changes and requested exceptions."},
    {"information_id": "cybersecurity_roles", "consumer_subcategory_id": "GV.SC-02", "dependency_kind": "required_input", "use_reason": "Coordinate supplier, customer, partner, and internal cybersecurity responsibilities."},
    {"information_id": "cybersecurity_roles", "consumer_subcategory_id": "RS.MA-01", "dependency_kind": "required_input", "use_reason": "Execute the incident response plan with the people and third parties who have assigned responsibilities."},
    {"information_id": "cybersecurity_roles", "consumer_subcategory_id": "RC.RP-01", "dependency_kind": "required_input", "use_reason": "Execute recovery work with people who have the necessary responsibilities and authorizations."},

    {"information_id": "supplier_criticality", "consumer_subcategory_id": "GV.SC-05", "dependency_kind": "planning_input", "use_reason": "Prioritize supplier requirements according to the importance of the supplier or service."},
    {"information_id": "supplier_criticality", "consumer_subcategory_id": "GV.SC-06", "dependency_kind": "planning_input", "use_reason": "Focus pre-relationship planning and due diligence on suppliers that matter most."},
    {"information_id": "supplier_criticality", "consumer_subcategory_id": "ID.RA-10", "dependency_kind": "required_input", "use_reason": "Determine which suppliers are critical and must be assessed before acquisition."},
    {"information_id": "supplier_criticality", "consumer_subcategory_id": "GV.SC-07", "dependency_kind": "planning_input", "use_reason": "Prioritize supplier risk assessment and monitoring over the relationship lifecycle."},
    {"information_id": "asset_inventory", "consumer_subcategory_id": "ID.RA-01", "dependency_kind": "required_input", "use_reason": "Identify the managed assets whose vulnerabilities must be found, validated, and recorded."},
    {"information_id": "asset_inventory", "consumer_subcategory_id": "ID.RA-09", "dependency_kind": "required_input", "use_reason": "Identify acquired hardware and software whose authenticity and integrity must be assessed."},
    {"information_id": "asset_inventory", "consumer_subcategory_id": "PR.PS-01", "dependency_kind": "required_input", "use_reason": "Apply configuration management to known platforms and software."},
    {"information_id": "asset_inventory", "consumer_subcategory_id": "PR.PS-02", "dependency_kind": "required_input", "use_reason": "Maintain, replace, and remove known software commensurate with risk."},
    {"information_id": "asset_inventory", "consumer_subcategory_id": "PR.PS-03", "dependency_kind": "required_input", "use_reason": "Maintain, replace, and remove known hardware commensurate with risk."},
    {"information_id": "asset_inventory", "consumer_subcategory_id": "DE.CM-09", "dependency_kind": "required_input", "use_reason": "Monitor known computing hardware, software, runtime environments, and their data."},
    {"information_id": "network_and_data_flows", "consumer_subcategory_id": "PR.DS-02", "dependency_kind": "planning_input", "use_reason": "Protect data in transit based on how and where it moves."},
    {"information_id": "network_and_data_flows", "consumer_subcategory_id": "PR.IR-01", "dependency_kind": "planning_input", "use_reason": "Protect networks and environments according to authorized communication paths."},
    {"information_id": "network_and_data_flows", "consumer_subcategory_id": "DE.CM-01", "dependency_kind": "required_input", "use_reason": "Monitor networks and network services that are known to carry authorized communication."},
    {"information_id": "asset_criticality", "consumer_subcategory_id": "ID.RA-04", "dependency_kind": "planning_input", "use_reason": "Estimate impact using the importance of affected assets and services."},
    {"information_id": "asset_criticality", "consumer_subcategory_id": "RC.RP-02", "dependency_kind": "planning_input", "use_reason": "Prioritize recovery actions according to asset and service importance."},

    {"information_id": "vulnerabilities_and_threats", "consumer_subcategory_id": "ID.RA-04", "dependency_kind": "required_input", "use_reason": "Evaluate the likelihood and impact of threats exploiting known vulnerabilities."},
    {"information_id": "vulnerabilities_and_threats", "consumer_subcategory_id": "ID.RA-05", "dependency_kind": "required_input", "use_reason": "Understand inherent risk from recorded threats, vulnerabilities, likelihoods, and impacts."},
    {"information_id": "risk_scenarios_and_priorities", "consumer_subcategory_id": "ID.RA-06", "dependency_kind": "required_input", "use_reason": "Choose, prioritize, plan, track, and communicate risk responses for recorded risks."},
    {"information_id": "change_and_exception_risk_records", "consumer_subcategory_id": "ID.RA-06", "dependency_kind": "planning_input", "use_reason": "Use documented change and exception risks when selecting, planning, tracking, and communicating their responses."},
    {"information_id": "secure_development_performance_results", "consumer_subcategory_id": "ID.IM-01", "dependency_kind": "planning_input", "use_reason": "Evaluate secure-development performance results to identify software-development practices that need improvement."},
    {"information_id": "authorized_adverse_event_alerts", "consumer_subcategory_id": "DE.AE-08", "dependency_kind": "event_input", "use_reason": "Provide authorized decision-makers and tools the adverse-event information used to apply incident declaration criteria."},
    {"information_id": "authorized_adverse_event_alerts", "consumer_subcategory_id": "RS.MA-02", "dependency_kind": "event_input", "use_reason": "Provide responders and triage tools the alerts, findings, and tickets used to validate incident reports."},
    {"information_id": "selected_risk_responses", "consumer_subcategory_id": "PR.AA-05", "dependency_kind": "planning_input", "use_reason": "Apply access permissions and reviews in accordance with chosen risk responses."},
    {"information_id": "selected_risk_responses", "consumer_subcategory_id": "PR.DS-01", "dependency_kind": "planning_input", "use_reason": "Select protections for data at rest that fit the chosen response to risk."},
    {"information_id": "selected_risk_responses", "consumer_subcategory_id": "PR.DS-02", "dependency_kind": "planning_input", "use_reason": "Select protections for data in transit that fit the chosen response to risk."},
    {"information_id": "selected_risk_responses", "consumer_subcategory_id": "PR.DS-10", "dependency_kind": "planning_input", "use_reason": "Select protections for data in use that fit the chosen response to risk."},
    {"information_id": "selected_risk_responses", "consumer_subcategory_id": "PR.IR-03", "dependency_kind": "planning_input", "use_reason": "Implement resilience mechanisms that fit selected risk responses."},

    {"information_id": "monitoring_findings", "consumer_subcategory_id": "DE.AE-02", "dependency_kind": "event_input", "use_reason": "Analyze potentially adverse events to understand the associated activity."},
    {"information_id": "monitoring_findings", "consumer_subcategory_id": "DE.AE-03", "dependency_kind": "event_input", "use_reason": "Correlate information from multiple sources when investigating potentially adverse events."},
    {"information_id": "monitoring_findings", "consumer_subcategory_id": "DE.AE-04", "dependency_kind": "event_input", "use_reason": "Estimate the impact and scope of potentially adverse events."},
    {"information_id": "monitoring_findings", "consumer_subcategory_id": "DE.AE-08", "dependency_kind": "event_input", "use_reason": "Apply incident criteria to analyzed potentially adverse events."},
    {"information_id": "incident_analysis", "consumer_subcategory_id": "RS.MA-01", "dependency_kind": "event_input", "use_reason": "Execute the response plan once an incident is declared and its situation is understood."},
    {"information_id": "incident_analysis", "consumer_subcategory_id": "RS.MA-03", "dependency_kind": "event_input", "use_reason": "Categorize and prioritize incidents using investigation results, scope, and impact."},
    {"information_id": "incident_analysis", "consumer_subcategory_id": "RS.MI-01", "dependency_kind": "event_input", "use_reason": "Contain an incident using the available analysis of what happened and what is affected."},
    {"information_id": "incident_analysis", "consumer_subcategory_id": "RS.MI-02", "dependency_kind": "event_input", "use_reason": "Eradicate the incident using investigation and root-cause information."},
    {"information_id": "incident_analysis", "consumer_subcategory_id": "RC.RP-01", "dependency_kind": "event_input", "use_reason": "Initiate and execute the recovery portion of the response plan when incident response calls for it."},
    {"information_id": "recovery_priorities_and_status", "consumer_subcategory_id": "RC.RP-05", "dependency_kind": "event_input", "use_reason": "Verify integrity, restore systems and services, and confirm normal operating status."},
    {"information_id": "recovery_priorities_and_status", "consumer_subcategory_id": "RC.RP-06", "dependency_kind": "event_input", "use_reason": "Declare recovery complete using restoration criteria and complete incident-related documentation."},
    {"information_id": "recovery_priorities_and_status", "consumer_subcategory_id": "RC.CO-03", "dependency_kind": "event_input", "use_reason": "Communicate recovery activities and restoration progress to designated stakeholders."},
    {"information_id": "improvement_lessons", "consumer_subcategory_id": "GV.OV-01", "dependency_kind": "planning_input", "use_reason": "Review risk-management outcomes and adjust strategy and direction when needed."},
    {"information_id": "improvement_lessons", "consumer_subcategory_id": "GV.OV-02", "dependency_kind": "planning_input", "use_reason": "Review and adjust the strategy to cover organizational requirements and risks."},
    {"information_id": "improvement_lessons", "consumer_subcategory_id": "GV.PO-02", "dependency_kind": "planning_input", "use_reason": "Update policy to reflect changes, findings, and lessons learned."},
    {"information_id": "improvement_lessons", "consumer_subcategory_id": "ID.IM-04", "dependency_kind": "planning_input", "use_reason": "Maintain and improve incident response and other cybersecurity plans that affect operations."},

    # Proposed product-authored dependency pass: these links make explicit
    # handoffs that the CSF outcomes imply but do not sequence for the user.
    {"information_id": "risk_objectives_and_tolerance", "consumer_subcategory_id": "GV.RM-03", "dependency_kind": "planning_input", "use_reason": "Bring agreed cybersecurity risk objectives, tolerance, and response direction into enterprise risk management."},
    {"information_id": "risk_scenarios_and_priorities", "consumer_subcategory_id": "GV.RM-03", "dependency_kind": "planning_input", "use_reason": "Represent analyzed cybersecurity risks in enterprise risk management processes."},
    {"information_id": "selected_risk_responses", "consumer_subcategory_id": "GV.RM-03", "dependency_kind": "planning_input", "use_reason": "Coordinate selected cybersecurity risk responses with enterprise risk decisions."},
    {"information_id": "risk_objectives_and_tolerance", "consumer_subcategory_id": "GV.RM-07", "dependency_kind": "planning_input", "use_reason": "Consider positive cybersecurity opportunities against agreed risk objectives and tolerance."},
    {"information_id": "risk_scenarios_and_priorities", "consumer_subcategory_id": "GV.RM-07", "dependency_kind": "planning_input", "use_reason": "Use risk analysis to identify potential beneficial opportunities."},
    {"information_id": "risk_management_measures_and_results", "consumer_subcategory_id": "GV.OV-03", "dependency_kind": "planning_input", "use_reason": "Use agreed KPIs, KRIs, and thresholds to judge cybersecurity risk-management performance consistently."},
    {"information_id": "risk_management_performance_results", "consumer_subcategory_id": "GV.OV-03", "dependency_kind": "required_input", "use_reason": "Review actual measurement and evidence results to determine whether cybersecurity risk management needs adjustment."},
    {"information_id": "risk_management_review_findings", "consumer_subcategory_id": "GV.OV-01", "dependency_kind": "planning_input", "use_reason": "Use performance-review findings when reviewing strategy outcomes and adjusting direction."},
    {"information_id": "risk_management_review_findings", "consumer_subcategory_id": "GV.OV-02", "dependency_kind": "planning_input", "use_reason": "Use performance-review findings when adjusting the strategy to cover organizational requirements and risks."},
    {"information_id": "risk_management_review_findings", "consumer_subcategory_id": "GV.PO-02", "dependency_kind": "planning_input", "use_reason": "Use performance-review findings when deciding whether cybersecurity policy needs updating."},
    {"information_id": "supply_chain_program_direction", "consumer_subcategory_id": "GV.SC-03", "dependency_kind": "required_input", "use_reason": "Integrate the established supply-chain risk program, strategy, objectives, policies, and processes with cybersecurity and enterprise risk work."},
    {"information_id": "supplier_lifecycle_results", "consumer_subcategory_id": "GV.SC-03", "dependency_kind": "required_input", "use_reason": "Bring recorded supplier and supply-chain risks into cybersecurity, enterprise risk, assessment, and improvement processes."},
    {"information_id": "integrated_supply_chain_risk_records", "consumer_subcategory_id": "GV.RM-03", "dependency_kind": "planning_input", "use_reason": "Escalate and address material supply-chain risks through enterprise risk management processes."},
    {"information_id": "external_legal_contractual_sources", "consumer_subcategory_id": "GV.OC-03", "dependency_kind": "required_input", "use_reason": "Identify and manage the external legal, regulatory, contractual, privacy, and civil-liberties requirements that constrain cybersecurity decisions."},
    {"information_id": "cybersecurity_roles", "consumer_subcategory_id": "GV.SC-08", "dependency_kind": "required_input", "use_reason": "Identify the supplier and internal roles that must participate in incident planning, response, and recovery."},
    {"information_id": "supplier_requirements_and_agreements", "consumer_subcategory_id": "GV.SC-08", "dependency_kind": "planning_input", "use_reason": "Use supplier agreement responsibilities when planning supplier incident involvement."},
    {"information_id": "incident_response_plan", "consumer_subcategory_id": "GV.SC-08", "dependency_kind": "planning_input", "use_reason": "Include relevant suppliers and other third parties in the incident response plan and recovery coordination."},
    {"information_id": "supply_chain_program_direction", "consumer_subcategory_id": "GV.SC-09", "dependency_kind": "planning_input", "use_reason": "Apply the agreed supply-chain program direction throughout the technology and service life cycle."},
    {"information_id": "supplier_criticality", "consumer_subcategory_id": "GV.SC-09", "dependency_kind": "planning_input", "use_reason": "Focus life-cycle practices and review effort on suppliers and services that matter most."},
    {"information_id": "supplier_lifecycle_results", "consumer_subcategory_id": "GV.SC-09", "dependency_kind": "planning_input", "use_reason": "Use supplier assessment and monitoring results to evaluate supply-chain practice performance."},
    {"information_id": "external_dependencies", "consumer_subcategory_id": "GV.SC-10", "dependency_kind": "planning_input", "use_reason": "Plan for the dependencies that must be transitioned, replaced, or ended after a supplier relationship concludes."},
    {"information_id": "supplier_requirements_and_agreements", "consumer_subcategory_id": "GV.SC-10", "dependency_kind": "planning_input", "use_reason": "Use agreement terms to identify post-relationship cybersecurity obligations and handoffs."},
    {"information_id": "asset_inventory", "consumer_subcategory_id": "GV.SC-10", "dependency_kind": "planning_input", "use_reason": "Identify supplier-provided services and related assets that must be transitioned or retired."},
    {"information_id": "asset_inventory", "consumer_subcategory_id": "ID.AM-08", "dependency_kind": "required_input", "use_reason": "Manage known hardware, software, services, and data through their life cycles."},
    {"information_id": "asset_criticality", "consumer_subcategory_id": "ID.AM-08", "dependency_kind": "planning_input", "use_reason": "Apply life-cycle attention and resources according to asset importance and impact."},
    {"information_id": "threat_intelligence", "consumer_subcategory_id": "ID.RA-03", "dependency_kind": "planning_input", "use_reason": "Identify and record internal and external threats relevant to the organization."},
    {"information_id": "threat_intelligence", "consumer_subcategory_id": "ID.RA-04", "dependency_kind": "planning_input", "use_reason": "Use relevant threat information when estimating likelihood and impact."},
    {"information_id": "threat_intelligence", "consumer_subcategory_id": "DE.AE-07", "dependency_kind": "event_input", "use_reason": "Apply relevant threat intelligence as context during potentially adverse event analysis."},
    {"information_id": "external_vulnerability_disclosures", "consumer_subcategory_id": "ID.RA-08", "dependency_kind": "event_input", "use_reason": "Receive, analyze, and respond to vulnerability disclosures from external sources."},
    {"information_id": "vulnerabilities_and_threats", "consumer_subcategory_id": "ID.RA-01", "dependency_kind": "planning_input", "use_reason": "Validate and record vulnerabilities identified through the disclosure process and other sources."},
    {"information_id": "restoration_assets", "consumer_subcategory_id": "RC.RP-03", "dependency_kind": "event_input", "use_reason": "Verify the integrity of backups and restoration assets before using them for restoration."},
    {"information_id": "verified_restoration_assets", "consumer_subcategory_id": "RC.RP-05", "dependency_kind": "event_input", "use_reason": "Use verified restoration assets to restore systems and services and confirm normal operation."},
    {"information_id": "log_records", "consumer_subcategory_id": "DE.CM-09", "dependency_kind": "required_input", "use_reason": "Make log records available for monitoring of computing hardware, software, runtime environments, and data."},
    {"information_id": "event_threat_context", "consumer_subcategory_id": "DE.AE-02", "dependency_kind": "event_input", "use_reason": "Use threat context to better understand potentially adverse events and associated activity."},
    {"information_id": "event_threat_context", "consumer_subcategory_id": "DE.AE-04", "dependency_kind": "event_input", "use_reason": "Use threat context when estimating the impact and scope of potentially adverse events."},
    {"information_id": "analyzed_event_information", "consumer_subcategory_id": "RS.MA-02", "dependency_kind": "event_input", "use_reason": "Triage and validate incident reports using analyzed event activity, impact, scope, and incident criteria."},
    {"information_id": "triaged_incident_reports", "consumer_subcategory_id": "RS.MA-03", "dependency_kind": "event_input", "use_reason": "Categorize and prioritize validated incident reports."},
    {"information_id": "incident_priority_and_scope", "consumer_subcategory_id": "RS.MA-04", "dependency_kind": "event_input", "use_reason": "Escalate incidents using their established priority, magnitude, scope, and impact."},
    {"information_id": "incident_priority_and_scope", "consumer_subcategory_id": "RS.MA-05", "dependency_kind": "event_input", "use_reason": "Apply recovery-initiation criteria using the prioritized incident and its validated scope."},
    {"information_id": "recovery_initiation_decision", "consumer_subcategory_id": "RC.RP-01", "dependency_kind": "event_input", "use_reason": "Execute the recovery portion of the incident response plan once recovery is initiated."},
    {"information_id": "incident_analysis", "consumer_subcategory_id": "RS.AN-06", "dependency_kind": "event_input", "use_reason": "Record investigation actions and preserve their integrity and provenance."},
    {"information_id": "incident_analysis", "consumer_subcategory_id": "RS.AN-07", "dependency_kind": "event_input", "use_reason": "Collect incident data and metadata and preserve their integrity and provenance."},
    {"information_id": "preserved_investigation_records", "consumer_subcategory_id": "RS.AN-07", "dependency_kind": "event_input", "use_reason": "Carry preserved investigation actions and records into the complete incident data record."},
    {"information_id": "incident_analysis", "consumer_subcategory_id": "RS.AN-08", "dependency_kind": "event_input", "use_reason": "Use incident investigation and preserved data to estimate and validate incident magnitude."},
]


# Version 2 records one exact producer-to-consumer path per row.  It is kept
# beside the v1 source/use catalog while the UI still reads the v1 map.
INFORMATION_FLOW_EDGE_ITEMS: List[Dict[str, str]] = [
    {"information_id": "risk_management_objectives", "title": "Risk-management objectives", "description": "Agreed cybersecurity risk-management objectives that guide decisions and priorities."},
    {"information_id": "risk_appetite_tolerance", "title": "Risk appetite and tolerance", "description": "Agreed boundaries for the amount and type of cybersecurity risk the organization is prepared to accept."},
    {"information_id": "risk_response_direction", "title": "Risk-response direction", "description": "Approved direction for avoiding, accepting, transferring, mitigating, or otherwise addressing cybersecurity risk."},
    {"information_id": "organization_cybersecurity_roles", "title": "Organization cybersecurity roles", "description": "Internal roles and authorities for cybersecurity decisions, implementation, review, escalation, and communication."},
    {"information_id": "supplier_third_party_roles", "title": "Supplier and third-party roles", "description": "Supplier and third-party roles, responsibilities, and points of contact for cybersecurity work."},
    {"information_id": "hardware_inventory", "title": "Hardware inventory", "description": "Known organization-managed physical devices and hardware assets."},
    {"information_id": "software_system_service_inventory", "title": "Software, system, and service inventory", "description": "Known software, systems, applications, and services managed or used by the organization."},
    {"information_id": "supplier_service_inventory", "title": "Supplier-service inventory", "description": "Known externally provided services and the suppliers that provide them."},
    {"information_id": "data_inventory", "title": "Data inventory", "description": "Known data types, records, and information resources managed by the organization."},
    {"information_id": "validated_vulnerability_records", "title": "Validated vulnerability records", "description": "Confirmed weaknesses that affect organization assets, systems, services, or data."},
    {"information_id": "relevant_threat_records", "title": "Relevant threat records", "description": "Recorded internal or external threats relevant to the organization and its assets."},
    {"information_id": "likelihood_impact_analysis", "title": "Likelihood and impact analysis", "description": "Analysis of how likely a risk scenario is and the effect it could have."},
    {"information_id": "prioritized_risk_records", "title": "Prioritized risk records", "description": "Risk records ranked or otherwise prioritized for treatment and management attention."},
    {"information_id": "event_activity_analysis", "title": "Event activity analysis", "description": "Analysis of activity associated with a potentially adverse event."},
    {"information_id": "event_impact_scope", "title": "Event impact and scope", "description": "Estimated impact and scope of a potentially adverse event."},
    {"information_id": "declared_incident", "title": "Declared incident", "description": "A potentially adverse event that has met the organization’s incident declaration criteria."},
    {"information_id": "incident_investigation_records", "title": "Incident investigation records", "description": "Investigation and root-cause analysis records describing an incident and its cause."},
    {"information_id": "incident_scope_impact", "title": "Incident scope and impact", "description": "Validated magnitude, scope, and impact of a declared incident."},
    {"information_id": "incident_priority", "title": "Incident priority", "description": "The established priority assigned to a validated incident."},
    {"information_id": "recovery_priorities_actions", "title": "Recovery priorities and actions", "description": "Selected recovery actions and the priority order for restoring systems, services, and data."},
    {"information_id": "restoration_verification_status", "title": "Restoration verification status", "description": "Integrity verification, restoration status, and confirmation of normal operation."},
    {"information_id": "incident_response_plan_coordination", "title": "Incident-response plan and coordination arrangements", "description": "The response plan and relevant coordination arrangements used after an incident is declared."},
    {"information_id": "risk_management_measurement_criteria", "title": "Risk-management measurement criteria", "description": "Agreed KPIs, KRIs, measures, and thresholds used to evaluate cybersecurity risk-management performance."},
]


def _flow_edges(source: str, information_id: str, consumers: List[str], dependency_kind: str, use_reason: str) -> List[Dict[str, str]]:
    """Create explicit, reviewable v2 paths without joining source/use lists."""
    source_kind = "external" if source.startswith("External:") else "subcategory"
    source_key = source.removeprefix("External: ") if source_kind == "external" else source
    return [
        {
            "edge_id": f"v2:{source_kind}:{source_key}:{information_id}:{consumer}",
            "information_id": information_id,
            "source_kind": source_kind,
            "source_subcategory_id": source_key if source_kind == "subcategory" else None,
            "external_source_label": source_key if source_kind == "external" else None,
            "source_guidance": "This outcome, an equivalent existing record, or a custom action may provide this information.",
            "consumer_subcategory_id": consumer,
            "dependency_kind": dependency_kind,
            "use_reason": use_reason,
            "provenance": "product-authored-v2",
        }
        for consumer in consumers
    ]


INFORMATION_FLOW_EDGES: List[Dict[str, str]] = [
    *_flow_edges("GV.OC-01", "organizational_mission", ["GV.RM-01", "ID.AM-05", "ID.RA-04", "RC.RP-04"], "planning_input", "Use mission objectives to align the work with what the organization is trying to accomplish."),
    *_flow_edges("GV.OC-02", "stakeholder_cybersecurity_needs", ["GV.RM-01", "GV.RM-05", "GV.SC-01", "RS.CO-02", "RS.CO-03", "RC.CO-03"], "planning_input", "Consider stakeholder cybersecurity and privacy needs when making this decision."),
    *_flow_edges("GV.OC-02", "stakeholder_cybersecurity_needs", ["GV.SC-05"], "required_input", "Define supplier cybersecurity requirements that address identified stakeholder needs."),
    *_flow_edges("External: legal, regulatory, and contractual sources", "external_legal_contractual_sources", ["GV.OC-03"], "required_input", "Identify the external requirements that constrain cybersecurity decisions."),
    *_flow_edges("GV.OC-03", "legal_contractual_requirements", ["GV.PO-01", "GV.PO-02", "RS.CO-02", "RC.CO-04"], "planning_input", "Use applicable requirements when setting or maintaining the work."),
    *_flow_edges("GV.OC-03", "legal_contractual_requirements", ["GV.SC-05"], "required_input", "Include applicable requirements in supplier cybersecurity requirements and agreements."),
    *_flow_edges("GV.OC-04", "critical_services_and_objectives", ["ID.AM-05", "ID.RA-04", "PR.IR-03", "RC.CO-03"], "planning_input", "Use the importance of services and objectives to guide planning and decisions."),
    *_flow_edges("GV.OC-04", "critical_services_and_objectives", ["RC.RP-02", "RC.RP-04"], "required_input", "Recovery priorities and verification must reflect the services and objectives that matter most."),
    *_flow_edges("GV.OC-05", "external_dependencies", ["ID.AM-04", "GV.SC-04", "ID.RA-10", "DE.CM-06", "RC.RP-02", "GV.SC-10"], "planning_input", "Use known dependencies to plan and focus the work."),
    *_flow_edges("GV.RM-01", "risk_management_objectives", ["GV.PO-01", "ID.RA-06", "GV.RR-03", "GV.RM-03", "GV.RM-07"], "planning_input", "Use agreed risk-management objectives to guide decisions and priorities."),
    *_flow_edges("GV.RM-02", "risk_appetite_tolerance", ["GV.PO-01", "ID.RA-06", "GV.RM-03", "GV.RM-07"], "planning_input", "Use agreed risk boundaries when selecting and coordinating responses."),
    *_flow_edges("GV.RM-04", "risk_response_direction", ["GV.PO-01", "ID.RA-06", "GV.RM-03"], "planning_input", "Use approved response direction when choosing and coordinating risk treatment."),
    *_flow_edges("GV.RM-06", "risk_assessment_method", ["ID.RA-04", "ID.RA-05", "ID.RA-06", "ID.RA-07"], "planning_input", "Use the established method to make risk analysis and records consistent."),
    *_flow_edges("External: measurement criteria", "risk_management_measurement_criteria", ["GV.OV-03"], "planning_input", "Use agreed measures and thresholds to evaluate risk-management performance."),
    *_flow_edges("External: operational measurement and evidence records", "risk_management_performance_results", ["GV.OV-03"], "required_input", "Review actual performance results to determine whether adjustments are needed."),
    *_flow_edges("GV.OV-03", "risk_management_review_findings", ["GV.OV-01", "GV.OV-02", "GV.PO-02"], "planning_input", "Use review findings when adjusting strategy, direction, and policy."),
    *_flow_edges("GV.RR-02", "organization_cybersecurity_roles", ["RS.MA-01", "RC.RP-01"], "required_input", "Identify the internal roles responsible for response and recovery work."),
    *_flow_edges("GV.SC-02", "supplier_third_party_roles", ["GV.SC-08"], "required_input", "Identify supplier and third-party participants in incident planning, response, and recovery."),
    *_flow_edges("GV.SC-04", "supplier_criticality", ["GV.SC-05", "GV.SC-06", "GV.SC-07", "GV.SC-09"], "planning_input", "Focus requirements, assessment, monitoring, and lifecycle work on suppliers that matter most."),
    *_flow_edges("GV.SC-04", "supplier_criticality", ["ID.RA-10"], "required_input", "Determine which suppliers require risk assessment before acquisition."),
    *_flow_edges("GV.SC-05", "supplier_requirements_and_agreements", ["GV.SC-08", "GV.SC-10"], "planning_input", "Use supplier responsibilities and agreement terms to plan incident and transition work."),
    *_flow_edges("GV.SC-01", "supply_chain_program_direction", ["GV.SC-03"], "required_input", "Integrate the established supply-chain risk program with cybersecurity and enterprise risk work."),
    *_flow_edges("GV.SC-01", "supply_chain_program_direction", ["GV.SC-09"], "planning_input", "Apply the agreed supply-chain program direction across the life cycle."),
    *_flow_edges("GV.SC-07", "supplier_lifecycle_results", ["GV.SC-03"], "required_input", "Bring supplier risk and monitoring results into cybersecurity and enterprise risk work."),
    *_flow_edges("GV.SC-07", "supplier_lifecycle_results", ["GV.SC-09"], "planning_input", "Use lifecycle results to evaluate supply-chain practice performance."),
    *_flow_edges("GV.SC-03", "integrated_supply_chain_risk_records", ["GV.RM-03"], "planning_input", "Escalate material supply-chain risks through enterprise risk management."),
    *_flow_edges("ID.AM-01", "hardware_inventory", ["ID.RA-01", "ID.RA-09", "PR.PS-03", "DE.CM-09", "ID.AM-08"], "required_input", "Identify the managed hardware to which the work applies."),
    *_flow_edges("ID.AM-02", "software_system_service_inventory", ["ID.RA-01", "ID.RA-09", "PR.PS-01", "PR.PS-02", "DE.CM-09", "ID.AM-08"], "required_input", "Identify the managed software, systems, and services to which the work applies."),
    *_flow_edges("ID.AM-04", "supplier_service_inventory", ["GV.SC-10"], "planning_input", "Identify supplier-provided services that must be transitioned or retired."),
    *_flow_edges("ID.AM-04", "supplier_service_inventory", ["ID.AM-08"], "required_input", "Manage known supplier-provided services through their life cycles."),
    *_flow_edges("ID.AM-07", "data_inventory", ["DE.CM-09", "ID.AM-08"], "required_input", "Identify the data to be monitored and managed through its life cycle."),
    *_flow_edges("ID.AM-03", "network_and_data_flows", ["PR.DS-02", "PR.IR-01", "DE.CM-01"], "planning_input", "Use known communication and data paths to plan protections and monitoring."),
    *_flow_edges("ID.AM-05", "asset_criticality", ["ID.RA-04", "RC.RP-02", "ID.AM-08"], "planning_input", "Use asset importance and impact to prioritize the work."),
    *_flow_edges("ID.RA-02", "threat_intelligence", ["ID.RA-03", "ID.RA-04"], "planning_input", "Use relevant threat intelligence to identify and analyze threats."),
    *_flow_edges("ID.RA-02", "threat_intelligence", ["DE.AE-07"], "event_input", "Apply relevant threat intelligence as context during adverse-event analysis."),
    *_flow_edges("ID.RA-03", "relevant_threat_records", ["ID.RA-04", "ID.RA-05"], "required_input", "Use relevant threats to analyze likelihood, impact, and inherent risk."),
    *_flow_edges("ID.RA-01", "validated_vulnerability_records", ["ID.RA-04", "ID.RA-05"], "required_input", "Use validated weaknesses to analyze likelihood, impact, and inherent risk."),
    *_flow_edges("External: vulnerability disclosure sources", "external_vulnerability_disclosures", ["ID.RA-08"], "event_input", "Receive and analyze external vulnerability disclosures."),
    *_flow_edges("ID.RA-08", "validated_vulnerability_records", ["ID.RA-01"], "planning_input", "Validate and record vulnerabilities identified through disclosure and other sources."),
    *_flow_edges("ID.RA-04", "likelihood_impact_analysis", ["ID.RA-05"], "required_input", "Use likelihood and impact analysis to determine inherent risk."),
    *_flow_edges("ID.RA-04", "likelihood_impact_analysis", ["ID.RA-06", "GV.RM-03", "GV.RM-07"], "planning_input", "Use risk analysis to guide response, enterprise risk work, and opportunities."),
    *_flow_edges("ID.RA-05", "prioritized_risk_records", ["ID.RA-06"], "required_input", "Choose and track risk responses for recorded, prioritized risks."),
    *_flow_edges("ID.RA-05", "prioritized_risk_records", ["GV.RM-03", "GV.RM-07"], "planning_input", "Use prioritized risks to coordinate enterprise risk work and identify opportunities."),
    *_flow_edges("ID.RA-06", "selected_risk_responses", ["PR.AA-05", "PR.DS-01", "PR.DS-02", "PR.DS-10", "PR.IR-03", "GV.RM-03"], "planning_input", "Implement and coordinate protections in accordance with selected risk responses."),
    *_flow_edges("ID.RA-07", "change_and_exception_risk_records", ["ID.RA-06"], "planning_input", "Consider documented change and exception risks when selecting responses."),
    *_flow_edges("PR.PS-04", "log_records", ["DE.CM-09"], "planning_input", "Make available log records useful for monitoring computing environments."),
    *_flow_edges("DE.CM-01", "monitoring_findings", ["DE.AE-02", "DE.AE-03", "DE.AE-04", "DE.AE-08"], "event_input", "Use monitored potentially adverse events in event analysis and incident decisions."),
    *_flow_edges("DE.CM-02", "monitoring_findings", ["DE.AE-02", "DE.AE-03", "DE.AE-04", "DE.AE-08"], "event_input", "Use monitored physical-environment events in event analysis and incident decisions."),
    *_flow_edges("DE.CM-03", "monitoring_findings", ["DE.AE-02", "DE.AE-03", "DE.AE-04", "DE.AE-08"], "event_input", "Use personnel and technology-usage findings in event analysis and incident decisions."),
    *_flow_edges("DE.CM-06", "monitoring_findings", ["DE.AE-02", "DE.AE-03", "DE.AE-04", "DE.AE-08"], "event_input", "Use external-provider monitoring findings in event analysis and incident decisions."),
    *_flow_edges("DE.CM-09", "monitoring_findings", ["DE.AE-02", "DE.AE-03", "DE.AE-04", "DE.AE-08"], "event_input", "Use technology and data monitoring findings in event analysis and incident decisions."),
    *_flow_edges("DE.AE-06", "authorized_adverse_event_alerts", ["DE.AE-08", "RS.MA-02"], "event_input", "Provide authorized staff and tools the alerts used for incident decisions and report validation."),
    *_flow_edges("DE.AE-07", "event_threat_context", ["DE.AE-02", "DE.AE-04"], "event_input", "Use threat context to understand activity and estimate event impact and scope."),
    *_flow_edges("DE.AE-02", "event_activity_analysis", ["RS.MA-02"], "event_input", "Use analyzed event activity to validate incident reports."),
    *_flow_edges("DE.AE-04", "event_impact_scope", ["RS.MA-02"], "event_input", "Use estimated event impact and scope to validate incident reports."),
    *_flow_edges("DE.AE-08", "declared_incident", ["RS.MA-01", "RS.MA-02", "RC.RP-01"], "event_input", "A declared incident initiates response, report validation, and recovery work."),
    *_flow_edges("RS.AN-03", "incident_investigation_records", ["RS.MA-03", "RS.MI-01", "RS.MI-02", "RS.AN-06", "RS.AN-07", "RS.AN-08"], "event_input", "Use investigation and root-cause analysis to prioritize, contain, eradicate, preserve, and assess the incident."),
    *_flow_edges("RS.AN-06", "preserved_investigation_records", ["RS.AN-07", "RS.AN-08"], "event_input", "Use preserved investigation records to maintain a complete, trustworthy incident record and assess its magnitude."),
    *_flow_edges("RS.AN-08", "incident_scope_impact", ["RS.MA-03", "RS.MA-04", "RS.MA-05"], "event_input", "Use validated incident scope and impact to prioritize, escalate, and initiate recovery."),
    *_flow_edges("RS.MA-02", "triaged_incident_reports", ["RS.MA-03"], "event_input", "Categorize and prioritize validated incident reports."),
    *_flow_edges("RS.MA-03", "incident_priority", ["RS.MA-04"], "event_input", "Escalate incidents according to their established priority."),
    *_flow_edges("RS.MA-03", "incident_scope_impact", ["RS.MA-05"], "event_input", "Apply recovery-initiation criteria using the prioritized incident and its validated scope."),
    *_flow_edges("RS.MA-05", "recovery_initiation_decision", ["RC.RP-01"], "event_input", "Execute the recovery portion of the response plan once recovery is initiated."),
    *_flow_edges("RC.RP-02", "recovery_priorities_actions", ["RC.RP-05", "RC.RP-06", "RC.CO-03"], "event_input", "Use selected recovery actions and priorities to restore, close, and communicate recovery work."),
    *_flow_edges("PR.DS-11", "restoration_assets", ["RC.RP-03"], "event_input", "Verify restoration assets before they are used."),
    *_flow_edges("RC.RP-03", "verified_restoration_assets", ["RC.RP-05"], "event_input", "Use verified restoration assets to restore systems and services."),
    *_flow_edges("RC.RP-05", "restoration_verification_status", ["RC.RP-06", "RC.CO-03"], "event_input", "Use restoration verification and normal-operation status to close and communicate recovery."),
    *_flow_edges("External: incident-response plan and coordination arrangements", "incident_response_plan_coordination", ["GV.SC-08", "RS.MA-01", "RC.RP-01"], "planning_input", "Use the plan and coordination arrangements to organize supplier, response, and recovery work."),
    *_flow_edges("ID.IM-01", "improvement_lessons", ["GV.OV-01", "GV.OV-02", "GV.PO-02", "ID.IM-04"], "planning_input", "Use evaluation findings to improve strategy, policy, and plans."),
    *_flow_edges("ID.IM-02", "improvement_lessons", ["GV.OV-01", "GV.OV-02", "GV.PO-02", "ID.IM-04"], "planning_input", "Use test and exercise findings to improve strategy, policy, and plans."),
    *_flow_edges("ID.IM-03", "improvement_lessons", ["GV.OV-01", "GV.OV-02", "GV.PO-02", "ID.IM-04"], "planning_input", "Use operational and incident lessons to improve strategy, policy, and plans."),
]


# The v1 pooled items listed here are intentionally excluded from the runtime
# catalog once the explicit v2 edge model is active.  The remaining original
# items are still valid atomic items and are reused by v2 edges.
_V1_POOLED_INFORMATION_ITEM_IDS = {
    "risk_objectives_and_tolerance", "cybersecurity_roles", "asset_inventory",
    "vulnerabilities_and_threats", "risk_scenarios_and_priorities",
    "incident_analysis", "recovery_priorities_and_status",
    "analyzed_event_information", "incident_priority_and_scope",
    "incident_response_plan", "risk_management_measures_and_results",
}

INFORMATION_FLOW_CURRENT_ITEMS: List[Dict[str, str]] = [
    item for item in INFORMATION_ITEMS
    if item["information_id"] not in _V1_POOLED_INFORMATION_ITEM_IDS
] + INFORMATION_FLOW_EDGE_ITEMS
