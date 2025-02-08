# Risk Assessment
⬅️[Back to Table of Contents](table_of_contents.md)

# Risk Assessment - PyRazer

## **Project Details**
- **Project Name:** PyRazer
- **Project Number:** 15984
- **Project Manager:** Alexander Shelton

## **Risk Assessment Table**

| Type of Risk       | Impact Description                                  | Examined | Estimated Likelihood (%) | Risk Description                                      | Mitigation Strategy                                     | Resource                   |
|--------------------|----------------------------------------------------|----------|--------------------------|------------------------------------------------------|---------------------------------------------------------|----------------------------|
| Technical Risk    | Compatibility issues with OpenRazer library               | ✅            | 50%                      | OpenRazer may not function correctly on all devices | Test early on diverse devices; have fallback tools    | Senior Software Developer |
| Technical Risk    | Bugs in input capture module                               | ✅           | 70%                      | Errors in keyboard/mouse input could block processing | Implement rigorous unit testing; allocate debugging time | Senior Software Developer |
| Technical Risk    | Performance issues during macro execution                     | ✅        | 40%                      | Slow response times during macro execution          | Optimize code; test under real-world usage scenarios | Senior Software Developer |
| Schedule Risk     | Delays due to unforeseen bugs                                 | ✅        | 60%                      | Debugging takes longer than expected                | Allocate buffer time; prioritize critical features | Project Manager            |
| Resource Risk	| Limited familiarity with Python libraries used in the application | ✅	        | 50%	                 | Learning curve delays implementation of CLI commands. | Provide training; consult documentation and community. | Project Manager |
| Security Risk	| Macros executing unintended actions                               |	✅	    | 30% | Poorly sandboxed macros may harm system integrity. | Implement strict validation for macros; sandbox execution. | Senoir Software Developer | 
| Scope Risk | Scope creep |	✅	| 50%	| Adding non-essential features causes delays. |	Define clear project boundaries; enforce change control processes. |	Project Manager |
| Technical Risk |	Depedency libraries being updated and causing compatibility issues. | 	✅	| 30%           |	Updates may introduce breaking changes. |	Monitor library updates; test new versions in isolated environments. |	Senoir Software Developer |
| External Risk |	Dependency on third-party libraries becoming deprecated	| ✅	| 20%	| Discontinued support affects functionality. |	Use well-maintained libraries; identify alternatives early.	| Senoir Software Developer	|																															
| Resource Risk	| Insufficient team members to meet deadlines	|	✅	|	50% | Delayed tasks due to workload imbalance. | Reassess workload; extend deadlines if critical tasks are delayed.|	Project Manager |
| Schedule Risk	| Overlapping tasks causing team conflicts	|	✅	|	40%	| Resource contention leads to inefficiency. | Develop a clear task schedule; stagger overlapping tasks. |	Project Manager |
| Quality Risk	| Incomplete or unclear documentation	|	✅	|	50% | Poor documentation hinders user and developer experience. |	Review iteratively; assign dedicated resources for writing and editing. |	Documentation Specialist |
| Technical Risk |	Inconsistent behavior across Linux distributions	|	✅	|	50%	| Functions differently on varying Linux distros. |	Test functionality on popular distributions like Ubuntu, Fedora, Arch. |	Linux Specialist |
| External Risk	| Team member unavailability due to unforeseen circumstances	|	✅	|	30% |	Absences delay tasks or block progress.	| Cross-train team members; maintain clear documentation for handover. | Project Manager |
| Security Risk	| Unsecured configuration files exposing sensitive data	|	✅	|	20% |	Unauthorized access to config files risks breaches. |	Encrypt sensitive data; restrict access to configuration files.	| Senoir Software Developer |
| Technical Risk |	CLI command errors causing crashes |	✅	| 50%	| Invalid commands lead to program instability. | Validate input; implement robust error handling. | Senoir Software Developer |
| User Experience Risk |	CLI commands being unintuitive |	✅	| 40% |	Poor usability frustrates users. |	Test commands with users; provide a detailed help menu.| Tester |
### Attachments  

#### Markdown
- [Table of Contents](table_of_contents.md)
- [Project Concept](project_concept.md)
- [Project Charter](project_charter.md)
- [Project Scope](project_scope.md)
- [Work Breakdown Structure](work_breakdown_structure.md)
- [Change Request](change_request.md)
- [Product Update Email](product_update_email.md)

#### PDF
- [Project Charter](project_charter.pdf)
- [Project Scope](project_scope.pdf)
- [Risk Assessment](risk_assessment.pdf)
- [Work Breakdown Structure](work_breakdown_structure.pdf)
- [Project Concept](project_concept.pdf)
- [Change Request](change_request.pdf)
- [Product Update Email](product_update_email.pdf)

#### Media 
- [Product Review (mp3)](product_review_recording.mp3)
- [Product Review (PowerPoint)](product_review_presentation.pdf)