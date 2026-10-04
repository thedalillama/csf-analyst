"""Source-traceable Tier guidance for the CSF Analyst learning experience.

The official text below is the NIST CSF 2.0 Appendix B, Table 2 notional
illustration.  The plain-language interpretation, transition hints, and
examples are product-authored.  They are intentionally kept in separate
fields so the product never presents its teaching guidance as NIST text.
"""

from typing import Any, Dict, List


NIST_TIER_SOURCE: Dict[str, str] = {
    "source_name": "NIST Cybersecurity Framework (CSF) 2.0",
    "source_version": "2.0 (February 2024)",
    "source_locator": "Appendix B, Table 2 - Notional Illustration of the CSF Tiers",
    "source_url": "https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf",
}

PRODUCT_GUIDANCE_NOTICE = (
    "These examples are product-authored learning guidance. They are not NIST requirements, "
    "a complete list of actions, or proof of outcome achievement, Tier status, or compliance. "
    "Use these examples to identify and document an approach that fits this Profile's "
    "requirements, risks, and operating environment."
)


TIER_GUIDANCE_SETS: List[Dict[str, Any]] = [
    {
        "tier_level": 1,
        "tier_name": "Partial",
        "official_governance_text": (
            "Application of the organizational cybersecurity risk strategy is managed in an ad hoc manner. "
            "Prioritization is ad hoc and not formally based on objectives or threat environment."
        ),
        "official_management_text": (
            "There is limited awareness of cybersecurity risks at the organizational level. "
            "The organization implements cybersecurity risk management on an irregular, case-by-case basis. "
            "The organization may not have processes that enable cybersecurity information to be shared within "
            "the organization. The organization is generally unaware of the cybersecurity risks associated with "
            "its suppliers and the products and services it acquires and uses."
        ),
        "plain_language_text": (
            "Security work happens when someone notices a problem or remembers to act. Decisions may be sensible, "
            "but they are not consistently based on documented risks, assigned roles, or a repeatable process."
        ),
        "transition_label": "Things to consider when strengthening this Profile toward Tier 2",
        "transition_hints": [
            {
                "hint": "Identify who makes risk decisions for this Profile's context.",
                "example": (
                    "Risk decision owner: Office manager\n"
                    "Technical adviser: Managed service provider\n"
                    "Escalation authority: Business owner"
                ),
            },
            {
                "hint": "Record the mission, stakeholders, requirements, threats, and key suppliers.",
                "example": (
                    "Mission: Process customer appointments and invoices.\n"
                    "Stakeholders: Customers, office staff, business owner.\n"
                    "Requirements: Protect customer contact and payment information.\n"
                    "Threats: Ransomware, account compromise, stolen laptop.\n"
                    "Key suppliers: Microsoft 365, backup provider, managed service provider."
                ),
            },
            {
                "hint": "Begin documenting risks, decisions, and reasons.",
                "example": (
                    "Risk: A stolen laptop could expose customer records.\n"
                    "Decision: Turn on device encryption and require a screen lock.\n"
                    "Reason: The PC is used outside the office and stores customer information."
                ),
            },
            {
                "hint": "Share important risk information with the people responsible for the work.",
                "example": (
                    "Tell office staff how to report a suspicious email or lost device.\n"
                    "Give the managed service provider the approved backup and encryption requirements.\n"
                    "Tell the business owner when a risk needs a cost or policy decision."
                ),
            },
            {
                "hint": "Use those facts to prioritize security actions.",
                "example": (
                    "First: Enable device encryption because loss of customer information would have high impact.\n"
                    "Next: Verify backups because ransomware could stop appointments and invoicing.\n"
                    "Later: Improve password guidance after confirming multifactor authentication is already enabled."
                ),
            },
        ],
    },
    {
        "tier_level": 2,
        "tier_name": "Risk Informed",
        "official_governance_text": (
            "Risk management practices are approved by management but may not be established as organization-wide "
            "policy. The prioritization of cybersecurity activities and protection needs is directly informed by "
            "organizational risk objectives, the threat environment, or business/mission requirements."
        ),
        "official_management_text": (
            "There is an awareness of cybersecurity risks at the organizational level, but an organization-wide "
            "approach to managing cybersecurity risks has not been established. Consideration of cybersecurity in "
            "organizational objectives and programs may occur at some but not all levels of the organization. Cyber "
            "risk assessment of organizational and external assets occurs but is not typically repeatable or reoccurring. "
            "Cybersecurity information is shared within the organization on an informal basis. The organization is aware "
            "of the cybersecurity risks associated with its suppliers and the products and services it acquires and uses, "
            "but it does not act consistently or formally in response to those risks."
        ),
        "plain_language_text": (
            "The organization knows cybersecurity risk matters and uses it in some decisions. However, the process "
            "still depends too much on individual judgment and is not consistently documented, scheduled, or followed."
        ),
        "transition_label": "Things to consider when strengthening this Profile toward Tier 3",
        "transition_hints": [
            {
                "hint": "Approve a written approach for managing cybersecurity risk in this Profile's context.",
                "example": (
                    "The business owner approves a one-page process requiring the office manager to record material "
                    "PC risks, select a response, and review open actions every quarter."
                ),
            },
            {
                "hint": "Assign who identifies risks, who makes decisions, who performs the work, and who reviews it.",
                "example": (
                    "Office manager: identifies and records risks.\n"
                    "Business owner: approves spending and accepted risk.\n"
                    "Managed service provider: implements technical actions.\n"
                    "Office manager and business owner: review open actions quarterly."
                ),
            },
            {
                "hint": "Define a repeatable method for recording, prioritizing, and responding to risks.",
                "example": (
                    "For each risk, record the affected information or service, likely impact, likelihood, selected "
                    "response, owner, and next review date before marking the decision complete."
                ),
            },
            {
                "hint": "Set a regular review cadence for risks, actions, evidence, and relevant suppliers.",
                "example": (
                    "Review open high-priority actions monthly, all open risks quarterly, backup evidence quarterly, and "
                    "the managed service provider annually or after a material service change."
                ),
            },
            {
                "hint": "Communicate decisions in a consistent way to people who need to act on them.",
                "example": (
                    "After approving a risk decision, record the decision in the workspace and send the applicable "
                    "requirement to the service provider or staff member responsible for the work."
                ),
            },
        ],
    },
    {
        "tier_level": 3,
        "tier_name": "Repeatable",
        "official_governance_text": (
            "The organization's risk management practices are formally approved and expressed as policy. Risk-informed "
            "policies, processes, and procedures are defined, implemented as intended, and reviewed. Organizational "
            "cybersecurity practices are regularly updated based on the application of risk management processes to changes "
            "in business/mission requirements, threats, and technological landscape."
        ),
        "official_management_text": (
            "There is an organization-wide approach to managing cybersecurity risks. Cybersecurity information is routinely "
            "shared throughout the organization. Consistent methods are in place to respond effectively to changes in risk. "
            "Personnel possess the knowledge and skills to perform their appointed roles and responsibilities. The organization "
            "consistently and accurately monitors the cybersecurity risks of assets. Senior cybersecurity and non-cybersecurity "
            "executives communicate regularly regarding cybersecurity risks. Executives ensure that cybersecurity is considered "
            "through all lines of operation in the organization. The organization risk strategy is informed by the cybersecurity "
            "risks associated with its suppliers and the products and services it acquires and uses. Personnel formally act upon "
            "those risks through mechanisms such as written agreements to communicate baseline requirements, governance structures "
            "(e.g., risk councils), and policy implementation and monitoring. These actions are implemented consistently and as intended "
            "and are continuously monitored and reviewed."
        ),
        "plain_language_text": (
            "The organization has an approved and repeatable way to manage cybersecurity risk. People know their jobs, use the "
            "process regularly, share information, and update the process when the business, technology, or threats change."
        ),
        "transition_label": "Things to consider when strengthening this Profile toward Tier 4",
        "transition_hints": [
            {
                "hint": "Use review results and lessons learned to adjust the risk-management process before the next problem repeats.",
                "example": (
                    "After a phishing incident, add a check that verifies multifactor authentication and staff reporting steps "
                    "during the next quarterly risk review."
                ),
            },
            {
                "hint": "Use current measures and indicators to identify changing risk conditions.",
                "example": (
                    "Track failed sign-in alerts, overdue patches, backup-test results, and unresolved high-priority actions; "
                    "review a change in those indicators before the scheduled quarterly review."
                ),
            },
            {
                "hint": "Connect cybersecurity risk decisions to resource and business decisions.",
                "example": (
                    "Before replacing the PC or renewing a cloud service, give the business owner the current risk summary, "
                    "required safeguards, estimated cost, and the consequence of accepting the remaining risk."
                ),
            },
            {
                "hint": "Make it easier to share timely risk information with authorized people.",
                "example": (
                    "Use the workspace action and evidence history to prepare a short monthly summary for the business owner and "
                    "send the managed service provider only the technical actions they need to perform."
                ),
            },
        ],
    },
    {
        "tier_level": 4,
        "tier_name": "Adaptive",
        "official_governance_text": (
            "There is an organization-wide approach to managing cybersecurity risks that uses risk-informed policies, processes, "
            "and procedures to address potential cybersecurity events. The relationship between cybersecurity risks and organizational "
            "objectives is clearly understood and considered when making decisions. Executives monitor cybersecurity risks in the same "
            "context as financial and other organizational risks. The organizational budget is based on an understanding of the current "
            "and predicted risk environment and risk tolerance. Business units implement executive vision and analyze system-level risks "
            "in the context of the organizational risk tolerances."
        ),
        "official_management_text": (
            "Cybersecurity risk management is part of the organizational culture. It evolves from an awareness of previous activities "
            "and continuous awareness of activities on organizational systems and networks. The organization can quickly and efficiently "
            "account for changes to business/mission objectives in how risk is approached and communicated. The organization adapts its "
            "cybersecurity practices based on previous and current cybersecurity activities, including lessons learned and predictive "
            "indicators. Through a process of continuous improvement that incorporates advanced cybersecurity technologies and practices, "
            "the organization actively adapts to a changing technological landscape and responds in a timely and effective manner to evolving, "
            "sophisticated threats. The organization uses real-time or near real-time information to understand and consistently act upon the "
            "cybersecurity risks associated with its suppliers and the products and services it acquires and uses. Cybersecurity information is "
            "constantly shared throughout the organization and with authorized third parties."
        ),
        "plain_language_text": (
            "Cybersecurity risk management is built into how the organization operates. The organization learns quickly, uses current "
            "information to make decisions, and adjusts its practices as risks, technology, and business needs change."
        ),
        "transition_label": "Things to consider when sustaining an Adaptive approach",
        "transition_hints": [
            {
                "hint": "Keep checking that rapid changes are still tied to documented risk decisions and organizational objectives.",
                "example": (
                    "When a new remote-access tool is proposed, record the business need, affected information, risk tolerance, "
                    "required safeguards, decision owner, and follow-up review before rollout."
                ),
            },
            {
                "hint": "Use lessons learned and indicators to improve the process, not only to close individual incidents.",
                "example": (
                    "A recurring backup-test failure triggers both a corrective action and an update to the review process so the same "
                    "failure is detected earlier next time."
                ),
            },
            {
                "hint": "Reassess whether the Tier target remains proportionate to this Profile's risk and resources.",
                "example": (
                    "If the PC no longer handles customer information, document whether the Tier target, review frequency, and supplier "
                    "oversight should be reduced while maintaining the safeguards still required."
                ),
            },
        ],
    },
]
