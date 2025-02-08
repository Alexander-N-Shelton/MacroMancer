# Work Breakdown Structure
⬅️[Back to Table of Contents](table_of_contents.md)

## WBS Table
| WBS Number | Task Name | WBS Description | Must Start by Date | Must End by Date | Planned Start Date | Actual Start Date | Status | Date Completed | Reason for Delay | "Level of Effort(hours)" | "Duration(days)" | "Predecessor" | Resource Name(s) | "Author" |
|:--- | :--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 1 | Project Initialization | "Define goals plan research and set up the environment." | 12-10-2024 | 12-17-2024 | 12-10-2024 | 12-10-2025 | Complete  | 12-17-2024 |  | 49.0 | 7.0 | None | Project Manager | Alexander Shelton |
| 1.1 | Define Project Objectives | "Outline project goals deliverables and scope." | 12-10-2024 | 12-14-2024 | 12-10-2024 | 12-10-2024 | Complete  | 12-14-2024 |  | 24.0 | 4.0 | None | Project Manager | Alexander Shelton |
| 1.1.1 | Identify Project Goals | "Define the primary goals of the project such as macro recording and key remapping." | 12-10-2024 | 12-11-2024 | 12-10-2024 | 12-10-2024 | Complete  | 12-11-2024 |  | 8.0 | 1.0 | None | Project Manager | Alexander Shelton |
| 1.1.2 | Document Deliverables | "List all outputs including CLI Key mapping and macro system." | 12-11-2024 | 12-12-2024 | 12-11-2024 | 12-11-2024 | Complete  | 12-12-2024 |  | 8.0 | 1.0 | 1.1.1 | Project Manager | Alexander Shelton |
| 1.1.3 | Define Scope | Detail the functionality to include and exclude. | 12-13-2024 | 12-14-2024 | 12-13-2024 | 12-13-2024 | Complete  | 12/14/2024 |  | 8.0 | 1.0 | 1.1.2 | Project Manager | Alexander Shelton |
| 1.2 | Research and Planning | Investigate technologies and plan the project structure. | 12-14-2024 | 12-16-2024 | 12-14-2024 | 12-14-2024 | Complete  | 12-16-2024 |  | 16.0 | 2.0 | 1.1 | Junoir Software Developer | Patrick Long |
| 1.2.1 | Research Python Libraries | Review Python libraries for interacting with peripherals. | 12-14-2024 | 12-15-2024 | 12-14-2024 | 12-14-2024 | Complete  | 12-15-2024 |  | 8.0 | 1.0 | 1.1 | Junoir Software Developer | Patrick Long |
| 1.2.2 | Research Key Binding and Macro Tools | Investigate Python libraries for key binding macro recording. | 12-15-2024 | 12-16-2024 | 12-15-2024 | 12-15-2024 | Complete  | 12-16-2024 |  | 8.0 | 1.0 | 1.2.1 | Junoir Software Developer | Patrick Long |
| 1.3 | Setup Development Environment | Configure tools and libraries for development. | 12-16-2024 | 12-17-2024 | 12-16-2024 | 12-16-2024 | Complete  | 12-17-2024 |  | 9.0 | 1.0 | 1.2 | Junoir Software Developer | Patrick Long |
| 1.3.1 | Install Required Libraries | Install Python and all other required libraries. | 12-16-2024 | 12-17-2024 | 12-16-2024 | 12-16-2024 | Complete  | 12-17-2024 |  | 3.0 | 1.0 | 1.2 | Junoir Software Developer | Patrick Long |
| 1.3.2 | Configure Virtual Environment | Set up a virtual environment and ensure dependencies work. | 12-16-2024 | 12-17-2024 | 12-16-2024 | 12-16-2024 | Complete  | 12-17-2024 |  | 3.0 | 1.0 | 1.3.1 | Junoir Software Developer | Patrick Long |
| 1.3.3 | Verify Setup | Test libraries and environment setup using sample scripts. | 12-16-2024 | 12-17-2024 | 12-16-2024 | 12-16-2024 | Complete  | 12-17-2024 |  | 3.0 | 1.0 | 1.3.2 | Junoir Software Developer | Patrick Long |
| 2 | Input Capture Module | Develop functionality for capturing input from devices. | 12-17-2024 | 12-24-2024 | 12-17-2024 | 12-17-2024 | Complete  | 12-24-2024 |  | 56.0 | 7.0 | 1 | Senior Software Developer | Josh Mooney |
| 2.1 | Keyboard Input Recording | Implement functionality to capture keyboard inputs. | 12-17-2024 | 12-20-2024 | 12-17-2024 | 12-17-2024 | Complete  | 12-20-2024 |  | 24.0 | 3.0 | 1.3 | Senior Software Developer | Josh Mooney |
| 2.1.1 | Handle Key  Presses | Capture single keypress events and save them. | 12-17-2024 | 12-18-2024 | 12-17-2024 | 12-17-2024 | Complete  | 12-18-2024 |  | 8.0 | 1.0 | 1.3 | Senior Software Developer | Josh Mooney |
| 2.1.2 | Handle Key Combinations | Capture combinations like Ctrl+Alt and save them. | 12-18-2024 | 12-20-2024 | 12-18-2024 | 12-18-2024 | Complete  | 12-20-2024 |  | 16.0 | 2.0 | 2.1.1 | Senior Software Developer | Josh Mooney |
| 2.2 | Mouse Input Recording | Implement functionality to capture mouse inputs. | 12-20-2024 | 12-24-2024 | 12-20-2024 | 12-20-2024 | Complete  | 12-24-2024 |  | 32.0 | 4.0 | 2.1 | Senior Software Developer | Josh Mooney |
| 2.2.1 | Handle Mouse Clicks | "Capture left right and middle mouse clicks and save them." | 12-20-2024 | 12-22-2024 | 12-20-2024 | 12-20-2024 | Complete  | 12-22-2024 |  | 16.0 | 2.0 | 2.1 | Senior Software Developer | Josh Mooney |
| 2.2.2 | Handle Additional Mouse Buttons | Capture additional mouse presses for specialized mice. | 12-22-2024 | 12-24-2024 | 12-22-2024 | 12-22-2024 | Complete  | 12-24-2024 |  | 16.0 | 2.0 | 2.2.1 | Senior Software Developer | Josh Mooney |
| 3 | Key Binding & Macro Development | Develop and integrate the key binding and macro system into the project. | 12-24-2024 | 01-10-2025 | 12-24-2024 | 12-24-2024 | Complete  | 01-10-2025 |  | 104.0 | 17.0 | 2 | Senior Software Developer | Josh Mooney |
| 3.1 | Simple Recording Module | Build a module to record and save key and mouse press. | 12-24-2024 | 12-28-2024 | 12-24-2024 | 12-24-2024 | Complete  | 12-28-2024 |  | 32.0 | 4.0 | 2 | Senior Software Developer | Josh Mooney |
| 3.1.1 | Record Key Presses | Add functionality to save keyboard actions. | 12-24-2024 | 12-26-2024 | 12-24-2024 | 12-24-2024 | Complete  | 12-26-2024 |  | 16.0 | 2.0 | 2.1 | Senior Software Developer | Josh Mooney |
| 3.1.2 | Record Mouse Presses | Add functionality to save mouse presses to file. | 12-26-2024 | 12-28-2024 | 12-26-2024 | 12-26-2024 | Complete  | 12-28-2024 |  | 16.0 | 2.0 | 2.2 | Senior Software Developer | Josh Mooney |
| 3.2 | Assignment Module | Implement functionality to assign commands to recorded actions. | 12-28-2024 | 01-01-2025 | 12-28-2024 | 12-28-2024 | Complete  | 01-01-2025 |  | 32.0 | 4.0 | 3.1 | Senior Software Developer | Josh Mooney |
| 3.2.1 | Assign Commands to Keys | Add functionality to attach a command to recorded keyboard actions. | 12-28-2024 | 12-30-2024 | 12-28-2024 | 12-28-2024 | Complete  | 12-30-2024 |  | 16.0 | 2.0 | 3.1.1 | Senior Software Developer | Josh Mooney |
| 3.2.2 | Assign Commands to Mouse Clicks | Add functionality to attach a command to recorded mouse presses. | 12-30-2024 | 01-01-2025 | 12-30-2024 | 12-30-2024 | Complete  | 01-01-2025 |  | 16.0 | 2.0 | 3.1.2 | Senior Software Developer | Josh Mooney |
| 3.3 | Execution Engine | Implement functionality to execute assign commands when recorded keys are pressed. | 01-01-2025 | 01-10-2025 | 01-01-2025 | 01-01-2025 | Complete  | 01-10-2025 |  | 40.0 | 9.0 | 3.2 | Senior Software Developer | Josh Mooney |
| 3.3.1 | Update or Modify Existing Bindings | Add functionality to update or modify existing bindings. | 01-01-2025 | 01-05-2025 | 01-01-2025 | 01-01-2025 | Complete  | 01-05-2025 |  | 32.0 | 4.0 | 3.2 | Senior Software Developer | Josh Mooney |
| 3.3.2 | Delete Saved Configurations | Add functionality to delete saved configurations.  | 01-09-2025 | 01-10-2025 | 01-09-2025 | 01-05-2025 | Complete  | 01-06-2025 |  | 8.0 | 1.0 | 3.2 | Senior Software Developer | Josh Mooney |
| 4 | Command-Line Interface (CLI) | Build a user-friendly CLI for managing features. | 01-10-2025 | 01-26-2025 | 01-10-2025 | 01-06-2025 | Complete  | 01-31-2025 | See 4.1.2. | 96.0 | 16.0 | 3 | Linux Specialist | Sarah Allen |
| 4.1 | Develop CLI Framework | Set up the CLI structure and integrate basic commands. | 01-10-2025 | 01-16-2025 | 01-10-2025 | 01-06-2025 | Complete  | 01-12-2025 |  | 48.0 | 6.0 | 3 | Linux Specialist | Sarah Allen |
| 4.1.1 | Setup CLI Architecture | Use Python's argpase or similar library to design the command-line framework. | 01-10-2025 | 01-12-2025 | 01-10-2025 | 01-06-2025 | Complete  | 01-08-2025 |  | 16.0 | 2.0 | 3 | Linux Specialist | Sarah Allen |
| 4.1.2 | Implement Help Command | Add a --help command to display usage instructions for all features. | 01-12-2025 | 01-14-2025 | 01-12-2025 | 01-24-2025 | Complete  | 01-31-2025 | Needed to write documentation and help before I could add it.  | 16.0 | 2.0 | 4.1.1 | Linux Specialist | Sarah Allen |
| 4.1.3 | Add Basic Error Handling | Implement error handling for invalid commands or missing arguments | 01-14-2025 | 01-16-2025 | 01-14-2025 | 01-16-2025 | Complete  | 01-18-2025 | I shouldn't have had the error handling before the main program commands. | 16.0 | 2.0 | 4.1.1 | Linux Specialist | Sarah Allen |
| 4.2 | Management Commands | "Add commands for recording listing and editing configurations." | 01-16-2025 | 01-22-2025 | 01-16-2025 | 01-08-2025 | Complete  | 01-16-2025 | Delete command added to Management Commands section adding 2 extra days | 48.0 | 6.0 | 4.1 | Senior Software Developer | Josh Mooney |
| 4.2.1 | Add Command | Implement an `add` command to add a new binding to the configuration. | 01-16-2025 | 01-18-2025 | 01-16-2025 | 01-08-2025 | Complete  | 01-10-2025 |  | 16.0 | 2.0 | 4.1 | Senior Software Developer | Josh Mooney |
| 4.2.2 | List Command | Implement `list` command to display all saved configurations. | 01-18-2025 | 01-20-2025 | 01-18-2025 | 01-10-2025 | Complete  | 01-12-2025 |  | 16.0 | 2.0 | 4.1 | Senior Software Developer | Josh Mooney |
| 4.2.3 | Update Command | Implement `update` command to allow modifcations to saved configurations. | 01-20-2025 | 01-22-2025 | 01-20-2025 | 01-12-2025 | Complete  | 01-14-2025 |  | 16.0 | 2.0 | 4.1 | Senior Software Developer | Josh Mooney |
| 4.2.4 | Delete Command | Implement `delete` command to remove unwanted configurations. | 01-24-2025 | 01-26-2025 | 01-24-2025 | 01-14-2025 | Complete  | 01-16-2025 |  | 16.0 | 2.0 | 4.2 | Senior Software Developer | Josh Mooney |
| 5 | Testing and Debugging | "Conduct testing validate compatibility and fix bugs." | 01-26-2025 | 02-04-2025 | 01-26-2025 | 01-26-2025 | Complete  | 02-01-2025 | Writing tests has taken a little longer than I thought it would.  | 72.0 | 9.0 | 4 | Tester | Linda Montgomery |
| 5.1 | Unit Testing | Write unit tests to ensure readability and correctness of all modules. | 01-26-2025 | 01-29-2025 | 01-26-2025 | 01-26-2025 | Complete  | 02-01-2025 | I should have allocated more time for writing tests.  | 24.0 | 3.0 | 4 | Tester | Linda Montgomery |
| 5.1.1 | Keyboard Input Tests | Write tests for keyboard input recording functionality.  | 01-26-2025 | 01-27-2025 | 01-26-2025 | 01-26-2025 | Complete  | 01-28-2025 | See 5 / 5.1 | 8.0 | 1.0 | 4 | Tester | Linda Montgomery |
| 5.1.2 | Mouse Input Tests | Write tests for mouse input recording functionality. | 01-27-2025 | 01-28-2025 | 01-27-2025 | 01-28-2025 | Complete  | 01-30-2025 | See 5 / 5.1 | 8.0 | 1.0 | 4 | Tester | Linda Montgomery |
| 5.1.3 | Execution Tests | Write tests for assignment and execution. | 01-28-2025 | 01-29-2025 | 01-28-2025 | 01-28-2025 | Complete  | 02-01-2025 | See 5 / 5.1 | 8.0 | 1.0 | 4 | Tester | Linda Montgomery |
| 5.2 | Compatibility Testing | Validate functionality across devices and distributions. | 01-29-2025 | 02-02-2025 | 01-29-2025 | 02-01-2025 | At Issue |  | See 5.2.2 / 5.2.3 (Will Still test devices after tests are written.) | 32.0 | 4.0 | 5.1 | Tester | Linda Montgomery |
| 5.2.1 | Device Validation | Validate input recording on various devices.  | 01-29-2025 | 01-30-2025 | 01-29-2025 | 02-01-2025 | Complete  | 02-04-2025 | Hadn't finished writing tests. | 8.0 | 1.0 | 5.1 | Tester | Linda Montgomery |
| 5.2.2 | Cross-Distribution Testing | Test  execution across major Linux distributions. | 01-30-2025 | 02-01-2025 | 01-30-2025 |  | At Issue |  | Move to backlog. Don't have time to test on multiple distributions. | 16.0 | 2.0 | 5.1 | Tester | Linda Montgomery |
| 5.2.3 | Consistency Testing | Ensure functionality remains consistent across distributions. | 02-01-2025 | 02-02-2025 | 02-01-2025 |  | At Issue |  | Move to backlog. Don't have time to test on multiple distributions. | 8.0 | 1.0 | 5.2.2 | Tester | Linda Montgomery |
| 5.3 | Bug Fixing | Resolve issues found during testing. | 02-02-2025 | 02-04-2025 | 02-02-2025 | 02-02-2025 | Complete  | 02-04-2025 |  | 16.0 | 2.0 | 5.2 | Senior Software Developer | Josh Mooney |
| 5.3.1 | Input Recording Bugs | Fix issues in input recording. | 02-02-2025 | 02-03-2025 | 02-02-2025 | 02-02-2025 | Complete  | 02-03-2025 |  | 8.0 | 1.0 | 5.2 | Senior Software Developer | Josh Mooney |
| 5.3.2 | Execution Errors | Resolve  errors in execution. | 02-03-2025 | 02-04-2025 | 02-03-2025 | 02-03-2025 | Complete  | 02-04-2025 |  | 8.0 | 1.0 | 5.2 | Senior Software Developer | Josh Mooney |
| 6 | Documentation | Create user and developer documentation for the project. | 02-05-2025 | 02-11-2025 | 02-05-2025 | 02-03-2025 | Complete  | 02-07-2025 |  | 48.0 | 6.0 | 5 | Documentation Specialist | Jacob Dillinger |
| 6.1 | User Documentation | Develop documentation for end users. | 02-05-2025 | 02-11-2025 | 02-05-2025 | 02-03-2025 | Complete  | 02-05-2025 |  | 48.0 | 6.0 | 5 | Documentation Specialist | Jacob Dillinger |
| 6.1.1 | Installation Instructions | Write a step-by-step installation instructions for Linux distributions. | 02-05-2025 | 02-07-2025 | 02-05-2025 | 02-03-2025 | Complete  | 02-05-2025 |  | 16.0 | 2.0 | 5 | Documentation Specialist | Jacob Dillinger |
| 6.1.2 | Usage Examples | Provide examples for recording and assigning. | 02-07-2025 | 02-09-2025 | 02-07-2025 | 02-04-2025 | Complete  | 02-06-2025 |  | 16.0 | 2.0 | 5 | Documentation Specialist | Jacob Dillinger |
| 6.1.3 | Troubleshooting | Document common troubleshooting steps. | 02-09-2025 | 02-11-2025 | 02-09-2025 | 02-05-2025 | Complete  | 02-07-2025 |  | 16.0 | 2.0 | 5 | Documentation Specialist | Jacob Dillinger |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Phase 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | GUI | Development of a graphical user interface for MacroMancer. | TBD | TBD | TBD | TBD | Future Phase | TBD |  | 184.0 | 23.0 | 1 |  2 |  3 |  4 |  5 |  6" | Project Manager | Alexander Shelton |
| 7.1 | GUI Framework Selection | "Evaluate PyQt GTK or Tkinter for implementation." | TBD | TBD | TBD | TBD | Future Phase | TBD |  | 16.0 | 2.0 | 7 | Senior Software Developer | Josh Mooney |
| 7.2 | GUI Prototyping | Develop wireframes and basic UI interactions | TBD | TBD | TBD | TBD | Future Phase | TBD |  | 32.0 | 4.0 | 7.1 | UX/UI Designer | TBD |
| 7.3 | GUI-Core Integration | Connect GUI with MacroMancer's backend. | TBD | TBD | TBD | TBD | Future Phase | TBD |  | 48.0 | 6.0 | 7.2 | Senior Software Developer | Josh Mooney |
| 7.4 | Feature Parity Testing | Ensure GUI fuctionality matches CLI capabilities. | TBD | TBD | TBD | TBD | Future Phase | TBD |  | 24.0 | 3.0 | 7.3 | QA Tester | TBD |
| 7.5 | GUI Beta Release | Conduct initial testing with users for feedback. | TBD | TBD | TBD | TBD | Future Phase | TBD |  | 24.0 | 3.0 | 7.4 | Tester | Linda Montgomery |
| 7.6 | GUI Final Release | Implement fixes and prepare for full release. | TBD | TBD | TBD | TBD | Future Phase | TBD |  | 40.0 | 5.0 | 7.5 | Senior Software Developer | Josh Mooney |

### Attachments  

#### Markdown
- [Table of Contents](table_of_contents.md)
- [Project Concept](project_concept.md)
- [Project Charter](project_charter.md)
- [Project Scope](project_scope.md)
- [Risk Assessment](risk_assessment.md)
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