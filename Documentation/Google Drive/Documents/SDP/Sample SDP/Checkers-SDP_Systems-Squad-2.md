Checkers Computer Software Application Software Development Plan 

Version 2.0 

October 17, 2022 

The Systems Squad 

Team Members: 

Kylie Hall   
Brittany Brenneman   
Xan Weatherholtz  
**Checkers Computer Software Application**   
**Software Development Plan**   
**The Systems Squad** 

Table of Contents 

1\. Introduction **3** 1.1 Purpose 3 1.2 Scope 3 1.3 Definitions, Acronyms, and Abbreviations 3 1.4 Document References 4 1.5 System Overview 4 

2\. Project Overview **4** 2.1 Project Purpose, Scope, and Objectives 4 2.2 Assumptions and Constraints 4 2.3 Project Deliverables 5 2.4 Evolution of the Software Development Plan 5 

3\. Project Organization **6** 3.1 Organizational Structure 6 3.2 External Interfaces 6 3.3 Roles and Responsibilities 6 

4\. Management Process **6** 4.1 Project Estimates 6 4.2 Project Plan 7 

4.2.1 Phase Plan 7 4.2.2 Iteration Objectives 7 4.2.3 Releases 7 4.2.4 Project Schedule 7 4.2.5 Project Resourcing 8 

4.3 Project Monitoring and Control 8 4.3.1 Requirements Management 8 4.3.2 Quality Control 8 4.3.3 Reporting and Measurement 9 4.3.4 Risk Management 9 4.3.5 Configuration Management 9 

5\. Miscellaneous **9** October 17, 2022 2 Version 2.0  
**Checkers Computer Software Application**   
**Software Development Plan**   
**The Systems Squad** 

Revision History 

| Date  | Version  | Description  | Author(s) |
| ----- | ----- | ----- | :---: |
| September 14, 2022  | 1.0  | Initial Version  | Kylie Hall,  Brittany Brenneman, Xan Weatherholtz, & Isabella Woel-Popovich |
| October 17, 2022  | 2.0  | Update of initial version (1.0)  | Kylie Hall,  Brittany Brenneman, and Xan Weatherholtz |

**1\. Introduction** 

**1.1 Purpose** 

The purpose of this Software Development Plan (SDP) is to materialize all information necessary to successfully manage the development and execution of the product in a controlled manner. The SDP is the leading framework constructed to serve as directional guidelines for the development team as well as a reference and timeline for the stakeholder. 

**1.2 Scope** 

This Software Development Plan (SDP) establishes a thoroughly detailed overall plan for the software implementations, testing, deployment, and qualifications for the Checkers Computer Software Application. This SDP is broken into a total of five sections. Excluding the first section being the introduction, the remaining four sections individually cover the project overview (Section 2), project organization (Section 3), and management process (Section 4), which go into detail pertaining to the information necessary to reference for the duration of development accurately. The approaches encompassed within this document are contingent on the product requirements provided by the client’s description as they were comprehended at the time of writing. The complete statement of the product requirements will soon officially be documented in the Software Requirements Specification (SRS). 

**1.3 Definitions, Acronyms, and Abbreviations** 

| Acronym  | Meaning |
| ----- | :---: |
| SDD  | Software Design Document |
| SDP  | Software Development Plan |
| SRS  | Software Requirements Specification |

October 17, 2022 3 Version 2.0

| STP  | Software Test Plan |
| :---: | :---: |

**1.4 Document References**   
**Checkers Computer Software Application Software Development Plan** 

**The Systems Squad** 

| Document Title  | Version  | Date  | Author(s) |
| ----- | ----- | :---: | :---: |
| Software Requirements Specification  | 1.0  | September 14, 2022 | Kylie Hall,  Brittany Brenneman, and Xan Weatherholtz |

**1.5 System Overview** 

The software system being developed is a standard or classic checkers game application that requires two users to play from one computer and will require the user to use a mouse to select each move. It will automatically display an 8x8 frame size with 24 disk-shaped autogenerated playing pieces placed on the user's designated starting side. The system will include two sets of 12 playing pieces, one set being red and the other set being black for each user to monitor which pieces belong to them. Additionally, both users must input their names which will determine which set they will be assigned, while also serving as a way to keep the score of any pieces conquered throughout the duration of each game. The first user to input their name will be assigned black and the second user will be assigned red. Furthermore, the user assigned to black will go first and start the game. The game will end once a player has collected all of the other player’s pieces, or if a player decides to quit the game the winner is decided based on which player has the most pieces left or collected. The system will offer a one-use undo option per game for each player and a reset option to clear the score and names to begin a new match. The application will be delivered in a hard copy format through a flash drive where no installation is required and must be compatible with Windows DLLs. 

**2\. Project Overview** 

**2.1 Project Purpose, Scope, and Objectives** 

The purpose of this project is to create a working checkers game to the specifications given by the client. The checkers game itself has one end target delivery date of December 5, 2022\. Furthermore, the project requires five documents to be constructed and delivered to the client: (1) The Software Development Plan; (2) The Software Requirements Specification; (3) The Traceability Matrix; (4) The Software Design; (5) The Software Test Plan. 

**2.2 Assumptions and Constraints** 

The Checkers Computer Software Application must be finished by December 5th, 2022\. There are four project team members: Kylie Hall, Brittany Brenneman, and Xan Weatherholtz. The equipment needed to produce the Checkers Computer Software includes personal computers, free downloadable software that can be used for the construction phase such as a text editor compatible with the C++ language and Unity, as well as the use of GitHub to track progress and changes to the software. 

October 17, 2022 4 Version 2.0  
**Checkers Computer Software Application**   
**Software Development Plan**   
**The Systems Squad** 

**2.3 Project Deliverables** 

● Software Development Plan (SDP)   
○ Target delivery date:   
■ Version 1: September 14, 2022   
■ Version 2: October 17, 2022   
● Software Requirements Specification (SRS)   
○ Target delivery date:   
■ Version 1: September 26, 2022   
■ Version 2: October 24, 2022   
● Traceability Matrix   
○ Target delivery date:   
■ Version 1: October 3, 2022   
■ Version 2: October 26, 2022   
● Software Design Document (SDD)   
○ Target delivery date:   
■ Version 1: October 12, 2022   
■ Version 2: November 2, 2022   
● Software Test Plan (STP)   
○ Target delivery date:   
■ Version 1: November 9, 2022   
■ Version 2: November 21, 2022   
● Delivery list of documentation, media, etc.   
○ Target delivery date: November 30, 2022   
● Project presentation   
○ Target delivery date: December 5, 2022   
● Source code   
○ Target delivery date: December 5, 2022 

**2.4 Evolution of the Software Development Plan** 

| Expected Release Date  | Version Number  | Remarks |
| ----- | ----- | :---: |
| September 14, 2022  | 1  | First version of the SDP, getting all of the criteria down before anything else is done. |
| October 17, 2022  | 2  | New version of the plan after other documents and more progress on the project has been made, so more information has been gained. |

October 17, 2022 5 Version 2.0  
**Checkers Computer Software Application**   
**Software Development Plan**   
**The Systems Squad** 

**3\. Project Organization** 

**3.1 Organizational Structure** 

**![][image1]**  
**3.2 External Interfaces** 

The external contact for this project is Professor Bob Tracy with St.Mary’s College of Maryland. Email Address: rttracy@smcm.edu 

Phone Number: 301-301-7503 

**3.3 Roles and Responsibilities** 

| Name  | Project Role(s) |
| :---: | :---: |
| Kylie Hall  | Coordinate weekly meetings for project progress, prepare the required documents for team members, and prepare the project’s user instructions. |
| Xan Weatherholtz  | Develop and design the software for the project. |
| Brittany Brenneman  | Validate that software requirements are satisfied and review/edit all required documentation. |

**4\. Management Process** 

**4.1 Project Estimates** 

There is no applicable overall cost to this project; The software shall cost $0, but the software shall cost 15 weeks of time. No re-estimation in cost shall occur throughout the project. 

October 17, 2022 6 Version 2.0  
**Checkers Computer Software Application**   
**Software Development Plan**   
**The Systems Squad** 

**4.2 Project Plan** 

**4.2.1 Phase Plan** 

Project phases shall occur sequentially in the waterfall model with some instances of iteration: as stated in *4.2.2 Iteration Objectives*. Communication and planning shall happen concurrently with stakeholders or customers involved in the phases. Modeling shall not happen concurrently with coding and constructing the software, instead it shall be in sequential order. Deployment shall be sequential from construction and shall take place on 11/30/22 with a delivery list of documentation, media, etc. along with a demonstration of the software and source code 12/5/22. 

**4.2.2 Iteration Objectives** 

The project shall have one iteration in planning and modeling. In this iteration, all requirements from the SRS document shall be thoroughly reviewed to ensure all requirements of the software are declared and the documentation prepares the software development team for construction. 

**4.2.3 Releases** 

The outcome of this project will yield one software release over the entire project duration. 

**4.2.4 Project Schedule** 

|  | Start  | Finish | Duration  (\# of days) | Week  1 | Week  2  | Week 3 | Week 4 | Week  5 | Week  6 | Week  7 | Week  8 | Week  9 | Week  10 | Week  11 | Week 12 | Week  13 | Week  14 | Week  15 |
| ----- | ----- | ----- | :---: | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Software  Development Plan Document  |  | 9/7/2022 9/14/2022  | 7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Software  Requirements  Specification  Document  | 9/12/22  | 9/26/22  | 14 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Traceability Matrix  | 9/19/22  | 10/3/22  | 21 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Software Design  Document  | 9/26/22  | 10/12/22  | 17 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Coding  | 10/12/22  | 10/26/22  | 14 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Updated Software Development Plan Document  | 10/13/22  | 10/17/22  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Updated Software Requirements  Specification  Document  Updated Traceability Matrix Document  | 10/18/22 10/25/22  | 10/24/22  10/26/22  | 6  1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Updated Software Design Document  | 10/27/22  | 11/2/22  | 7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Software Test Plan Document  | 11/3/22  | 11/9/22  | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Testing  | 11/10/22  | 11/21/22  | 11 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

October 17, 2022 7 Version 2.0  
**Checkers Computer Software Application**   
**Software Development Plan**   
**The Systems Squad** 

| Updated STP  Document  | 11/10/22  | 11/21/22  | 11 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Delivery  (Documentation,  Media, etc.)  | 11/30/22  | 11/30/22  | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Project Presentation, Source Code  | 12/5/22  | 12/5/22  | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

**4.2.5 Project Resourcing** 

The type of staff required for this project include a project manager, a software developer, a tester, and a technical writer. Therefore, this project shall have four members with experience in each specialization, with no special skills required. There shall not be any special training required, and therefore no target dates for specialized training will be provided. 

**4.3 Project Monitoring and Control** 

**4.3.1 Requirements Management** 

Changes made to product requirements shall be provided via email in a fully updated version of the SRS document. This document shall provide scheduled dates where updated documentation shall be provided: *4.2.4 Project Schedule.* Reference the list of document updates below. 

|  | Start Date  | Finish Date  | Duration |
| :---- | :---- | :---- | :---- |
| Software Development Plan Document | 10/13/22  | 10/17/22  | 4 days |
| Software Requirements Specification Document | 10/18/22  | 10/24/22  | 6 days |
| Traceability Matrix  Document | 10/25/22  | 10/26/22  | 1 day |
| Software Design  Document | 10/27/22  | 11/2/22  | 7 days |
| STP Document  | 11/10/22  | 11/21/22  | 11 days |

**4.3.2 Quality Control** 

The quality of the project will be evaluated in the number of defects in the software. Defects will be recorded and tracked as Change Requests in the STP document to track the quality control of the software. 

October 17, 2022 8 Version 2.0  
**Checkers Computer Software Application**   
**Software Development Plan**   
**The Systems Squad** 

All defects will go through a required review process to ensure that each deliverable is of acceptable quality, using guidelines and checklists. The review process will involve the following procedures: (1) the manual software tester will test for the validity of the software requirements, (2) the tester will report all defects identified in the software to the project manager and software engineer, (3) the software engineer will fix the identified defects. This review process will repeat until the manual software tester verifies that the identified defects have passed and no further defects are identified. In addition, the manual software tester will verify that the software is compatible with standard classroom Dell XPS desktop computers along with the windows operating system version 10\. Furthermore, all external interfaces utilized by the software will be verified during the review process. 

To ensure corrective actions are prioritized, any defects found during the review process that are not corrected before release for integration shall be recorded as Change Requests in the STP document so that they are not forgotten in sequential development stages. 

**4.3.3 Reporting and Measurement** 

Appropriate documents will be updated as the project progresses. In each iteration of this document the revision history, any schedule changes, and changes in project estimates will be updated. 

**4.3.4 Risk Management** 

The approach to identify risks shall be used throughout the entire lifecycle of the project. To prioritize risk, it will be essential to evaluate at least once per iteration and must be documented in the STP by the project manager in communication with the software developer. The risks will then be analyzed and further monitored throughout the project to mitigate potential risks in future iterations and development. All risks will identify and rank the possibility of risks occurring. 

**4.3.5 Configuration Management** 

All major project changes will be reported in the appropriate documents. 

Information about project and product artifacts (such as system software, models, components, etc.) is all included in the appropriate design documents. The artifacts that are customer deliverables, which will be stored via a hard copy format as a flash drive, will be included in the final version of the project. 

The project team will review plans for major changes and approve them before those changes are implemented. 

**5\. Miscellaneous** 

There are no miscellaneous items at this time. 

October 17, 2022 9 Version 2.0

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYMAAAC6CAYAAABMZiHDAAA2x0lEQVR4Xu2dBbhU5frFx+Iv3qvXq6hcW0zsxgKxu7ELEAMTFREUFRMVUSxURFGxsLuwu7u7uwPb/d+/b/Ya9tmcOTXncM7MrPU864E5s2fX7HnX97315XJGWWGaaaZpP/300//csWPHyDTLldNNN91DU089dQ4ahtEExD+e9ptsssnfkWGUMTp06PD0VFNNlYOGYTQBFgOjEmAxMIwSYTEwKgEWA8MoERYDoxJgMTCMEtEUMZgwYUL02muvBb7wwguBH3zwQeAff/yR3bxB+OyzzwLffPPN6O+/G3U69YLz0nm+/vrr0V9//VXj/ffff7/w/ltvvTXJ+20N3P8PP/yw8JrzffXVVwvXkCXfU2Pw3nvvhc/8/PPPgQ3Fp59+Gsh32FhwTS+//HIg38c///yT3aROWAwMo0RYDCwGWVgMDKMK0VQxGDNmTOCGG24YXXDBBdGhhx4aeMYZZ2Q3rxcY/4svvjhw9913j37//ffsJvXim2++Cfz4448nERMMTK9evQLja40+//zzwnsY0v322y/acsstA++88842LwZPPfVUNH78+MJrDPaRRx4Z3XrrrYE77rhjtNdee0U333xz4KBBg1Kfrh933HFHtMsuuxSMc0PAPRs1alRgnz59sm/XC767I444IvDYY4+N/vzzz+wmdcJiYBgloiliwKgNAYAzzjhjdM8990T9+/cPnHPOOaNPPvkk+5E6wf4eeOCBwPPPP7/RhoDZyKWXXhp47bXXTmLMGa1uv/32gTPPPHM0bty4wnsYux49ekTzzDNPIOfQ1jF8+PAao/1ffvkluvDCC6Ovv/46cMkll4zWXXfd8D3AkSNHpj5dPxCaBRdcMHrkkUcCGwIE+O677w5EEBqL77//PogI3HbbbRs9w7QYGEaJaIoYAI3kZ5pppui5556Lhg0bFtiuXbvoiSeeiE466aRAjNTpp58eXXLJJYEfffRRdMwxx4S/wVdeeSX64YcfojPPPDPwsMMOC4ZALgcE59xzzw0jfggw5kcddVQgxv/xxx+PllpqqUBG/vfff3+Nc/3iiy+iESNGBC6//PLRVlttFYwXvO6668LIuVOnToEPP/xwmPncfvvtgYxSTzvttPA3iKEcOHBgmAFBjNczzzxT2B+fP++886LBgwdH77zzTuBvv/0WXXHFFdGpp54ayD5Hjx4dffnll4GM5jk3zht+9dVXYaQvgTvllFPCvUYk4f7771/DWHJcjKmw9NJLRxtssEH066+/BiIQ3COuA15zzTVhO1xNELHgnHA1wfvuuy8I44ABAwL33HPPcB24fyCjd66d84B8R99++20QKci1g+effz5Q+5crkO+V75T7Djke589xoMXAMFoBFgOLgcXAMIxmEQNiBxtttFHgpptuGowZvn+IYTrooIMK4rDbbrsFw3DOOecE8sPHWPI3uNxyy0U//vhjdPzxxwdiPBGNo48+OvDRRx8NBl9uqpVXXjkESTHycOjQoeHzaSAGt9xyS2Dfvn2jBRZYIBhtKIOfFgN88hwDYji5hrvuuisQwzX//POH48CNN9442nfffQuGktccZ7311isI0LPPPhutuuqqwZ0G11lnnejEE08M1wLXX3/94J7addddA3EB7bDDDuHaIPvn3hH8hhjcupAVA8RW8RCICwkBR9QghnmnnXYqfAdsM+uss0Znn3124EorrRT+zvcKOaedd945GH24yCKLhDiPjPuKK64Y4jJ77LFHIPtbZZVVCnEmYjTsTzEC7gcxA4uBYbQimkMMGNFrFPjTTz8F4yMxWGONNYKxlyHDUOFTZqQMZ5tttjA6liFaYoklonfffTcYU7j33ntHBxxwQAhoQgKjGGkZJnzajFplODmXbMwAMSAoChnZY+gwZpCYwcknn1xDDJi98DfIuc4999zRlVdeGcj7+NNlWDHaxBzkr2cUf+ONN4brkLG7/vrrw3UjMhBDzQxII/XFFlssiMayyy4byDURBMYoQs6fGcHYsWMD64trZMXgoYceiuadd97CyL1Lly5BWBEoeMMNN0RvvPFGYWZw7733BsHkc5DvEBH97rvvAldYYYVoyJAhYQYEY0Mc7jnXBDn+008/HS2zzDKBzBSZPZElBJnZIeQMDOCiiy5qMTCM1kZTxeCiiy4KlJsojbQY8MPGjYGxgbhycJFIDGaZZZbgqkiLAemd3bt3D2QELfcI3GeffcLIk9E/xAhhYNJikA1AM0qV24cR7OKLLx6tueaagQgJ7q20GCAyGvUiCPPNN1/hfDHUCy20UBAViNHG7UQQF2IcmQmtvfbahX1wfmzDLAPyf/aj2VLnzp2DC0rXyHUxUscAQ15jHCVQnHNdyIoB58k5KyBMwJ7vTOKDIPE3uboQg3QAGTFAhHHlQO4/rj5lDxGU53OHH354IMd/7LHHCk3kbrvttvA+3xVEEHGvyfhbDAyjDcBiYDGwGBiG0SQx4IctQ/Cf//wn+L3TIJjYs2fPQHzVbC/jjSHEwOOnhrgsMIRpMSDIqDRDDDYuB/nk+QwuDwLTENcURVIYLIhbBsOSBsZYxhxjSyzikEMOCUQcMGy4giCGkNgArhvI8Qim6nrx+eNCUQ4/hos4CW4QiNghSJwLvnFIeucJJ5xQcNNwDNxpuGcgIoT7R24kxGubbbYpCCoGGNeVfPi4jWoD1wK5h/jhdc8Rj7nmmqtwj1966aVwHI4Bu3XrFsRBhYMEtDknzhPyPu4cBbyJ6yByOh/SixFCBZy5b8Q9EA1IfQdxHaW68gzg8jv44IMDuZ98R7179w7cYostGl1rYjEwjBLRFDHAeCuAS9EZIz9GchrNpUfWZJsQMxAYpaaziTDQiIUCxhgyRrPy8ROQZT8ylOwbX7/qBghIIj7KZsIYZStgERNlKyEUGEdl7nAtjLYxQJDZA6PazTffPJCRO8eR+HBOCIBG+QRMiWm8+OKLgYxsmRlAjZQxvox+FWTXeSubh9nOdtttV8geQgz79etXuIdcH8ZVRWXcnyy4hzLm3B/2KR8923MeGGFIUB6RuOmmmwL5DrkO3WMC4IgE3ytkdnLUUUcVBBmDzb1WQJjPv/3224XvgGtBNJgBQgLW3GNVrfP9IwZkTEHuJ0F23S8EFHFpDCwGhlEimioGSpvEpSODIyPFvwSBIe+zfRr8TYaFESCjUmWikLnC3+RSYFtG/nJhAAK1pKRCGQ1G2pBRs7YTGFWzH4gLi/clXrzWdUDOmfNnPxAh41+Nshm1s50ML9fOZ+Qm4n3+ZTSvqmgMIMFwDDTEECI0ukcEZQlk6xo4ps5H94/zVJC6tlYN3CulbupzGsnzHueuimKloeoe8z1wLbrHjN75PPcNco5cp/bH/eI7kZixLceV+PCa4+mZ4HvicwLv8VrpuqSaZp+p2gSvLlgMDKNEWAwsBhYDwzCaJAbNDdIx5b9GELIB4HIHBpgArGIEFMoRtFWqplE6LAaGUSLaghjgU1dBFiPO2ka+5QxG+1QAp7uIMuLmOivtWlsLFgPDKBFtQQwMo1RYDAyjRFgMjEqAxcAwSoTFwKgEWAwMo0RYDGqH/PlkNpHdo8wbyGsVeJF9w3bKTspmMmlfeh9q344ZNB8sBoZRIiwGtUMts2k3QfsKFWhRdUwBmVZGI+BNWqY6gFIRnQUrkVF8pwpdUk9JEVWqplE6LAaGUSIsBrXDYlBesBgYRomwGNQNehPNMccc0dVXXx2Im4gGequvvnogRVK0i6BNNcTwUyBG0ZQK1SjyYjEYtfDgbzS0u+yyywLlhlIjOMQCd5MWpGd/uKRUlFabK6raYTEwjBJhMagbGHsa1anpHEaevkPqyEmvIGYGqpOgmpaCMoRD6xXQAwlRUXM76ipo5kZPI8gx+JuK0uh5xIxBnVHp60NPJC0I5EK1SWExMIwSYTGoG4zCN9tss7BSF6ShGk3bYuMTyCIxGHgt08nInY6ffEYtmTHuvNbKX7SFnnPOOQuN2Wi/QJsKtQXv2bNnEJOzzjorkAWA6MaqLp/FupZWMywGhlEiLAZ1w2JQHrAYGEaJsBjUj0suuaRg/FnWEXcQi8dAlo2kNXY6TZT+/AceeGChcRzGm8VqJAa0e2bxGLXFZhvWEVabbcSGmMKYpEU06yzQhltLfVZa76bmgMXAMEqExaB+sEIbC+rA+F6FzqRapYzFfZgZpLHwwguHtRkEAsZ1iQEzCoSGdZAh6yIQh5AYsNKaZwN1w2JgGCXCYlA/CNjSdloLshBEZjU02LVr15BeKuBWQgxY2UwgG2iHHXYorFyGGDATIMMIvv7662H1MC0QT5dT3FHKPkIMmBEYxWExMIwSYTGoHxaDtg+LgWGUCItB/aAGQMtwPvTQQyE2oPV8WaYSN5CAS2n99dcPfv/0gjiIAYFhiAuIwLMWu2GBGNZAXm211QIPPfTQ0OJaYsE60ASdjeKwGBhGibAY1A/1KIJa51mrglEwlu4vxPsUoSEC2gYx0UI2kNcUk6Vfsx8FiCk8SxedsVpaeh1pY1JYDAyjRFgMjEqAxcAwSoTFwKgEWAwMo0RYDIxKgMXAMEqExcCoBFgMDKNEWAyMSoDFwDBKhMXAqARYDAyjRFSrGKgG4NVXXw3to1lsRgvO0A7i/fffDyzWB0hpnw8//HD4jNYaeOyxx8J6BPWBbTk25HgcW+sZUHTGOSn1NAvSTt99991QmAY5Hr2LKGaD1QiLgWGUiGoVAxnzUaNGRUOGDCkYXqqBBw8eHL355puB1ADUBhlu1iN48sknQ20BvPLKK8Pf64OODSlQU20CpNBs6NChhWNkoSK44447LhAxOvXUU0NDPViNsBgYRomoVjEQWCyGxWomTJgQeMUVV4SupCoyKwYMMuzbt2+YHTCDgDSUKzabyGLkyJGBtKVOg2Z1dEdNd0JNg7898MADhRbYFKrR5VQtr6sRFgPDKBHVLgajR4+O+vfvX+g1dNttt9UQAfoOYZxx/0D6Eo0bNy6sQQCZGSAGcisxMqcXESP922+/PZCRfrp/kXD++ecHYvjTQKCYLQi4gi6++OKwLgJkVsG5sA3ExcRxLQYWA8NoMiwGFoNKgMXAMEqExWB0WOD+kEMOCaQPUNo1gzCw9vGNN94YSPCWdY3pFQT79esXxOCFF14I7NWrV/Txxx9H9957b/Too48G3nnnnWHFMwK96eCyxGCbbbYpGHrIthh5uZ54n2Z2++67byCxDMSAWAe0GFgMDKNkWAxGRz169IjWWmutQLqQqhmdQAyBlcsgo3+WpJQ/X2JAJ1JIDIEgNK2utVgNC9QQ4FWQWZAYYOCZOYgEhREDHQORIUi99tprB5JtZDGoCYuBYZQIi8Ho0DKa0TtcY401QptqBYgBy1LiDoIYaVpXC4gB7aUZucO99947euWVV0Jg96mnngpkNoF7Kb1PIDEYNGhQ4W+AoDLHURCbmQgzjT59+gRKDOwmmgiLgWGUCIuBxaASYDEwjBJRrWKgtQZYgB4jL8PLymLdunWLHn/88UB8/MQGtNAM/vz0WgUsToMbiSIw2Lt37+DTx0jjKoLsB8FQHYGOz7F1fERC+xw2bFg0cODA6J133gncYostguuJBXIgwoBgDRgwIJB0VkQF0YDso9pgMTCMElGtYsBIHeLPZ4lKVRATQO7Zs2co+oLECDCu48ePDyReQFBXnx8+fHj4uww3K5jxmSeeeCLaeeedA5k9PPjggzWOj8BcdNFFgcQIOLb2STYRRp0ZCeTznCdZT/Dyyy8PMQREA7IN9RGslgbrqo+oVFgMDKNEVKsYKBuIgC4CoKIzjLH+BqkAZglKiQEuIECQGapyWZlCfIbUTwREriNmCtniMQy2Asp8hs9KDPQ3vcYNRGGZtmdbZhg6R85b78GGFr1VEiwGhlEiLAYWg0qAxcAwSkS1ikFDQd8f6g+uuuqqwNoaxxmtD4uBYZSIaaaZxmJQB/DlU0WsCuPsCN9oG0AM4oENg5vsI24YRkPQrl279rPPPvuvpFSaZrlyhhlmeCwe2DC4yT7ihmE0BBYDsxJoMTCMEtG+ffsp4h/QwvF/O5vNyvVijk84LuZBMZ9LOLiW7c0mcsopp+w87bTTzvN///d/OWgYhtEWgNN6g5i3x+yT8D8xGbIiuvCSmMNizp5wivBJwzAMo6yBAMyfcEguPxNYJL1BBu1iHhjzmoRrx/xXjS0MwzCMsoPFwDAMo8oxYy4fH7gg4YCY/66xRe3ANbRiwktj7h9zoYROljcMwygDYKyXSIgRPzfmagmbYshnjnl4zNMSEnOYocYWhmEYRpsCweAtc/kAMOwfs2ONLZqGaWOun3B4zP1yeVcTnDK1nWEYhtEGYDEwDMOoUmCMF0s4KObxuXzQF7ZPbddc6BTz4JgnJdwslw86G4ZhGK0E6gO2jnlGwr65vLFuaRAzIHYAER9EaO6EhmEYxmTCPAkxxCfG7Jpw+vRGLQxmJHDBmAfEHJVwrfRGhmEYRsvBYmAYhlHlWDeXLxyDuIXmzE00zK0FAtdrJrw4l48pUOMADcMwjGaCDOsRuXxV8AoJyfJpK6CGAZK9xGxFglVXtbNhGIbRAGDsV415bULEoCUyhJobzFLWSXh3zF1zEwXNje8MwzAaCYuBYRhGlQJXy7wJ94p5dcxuCVszLtBU/C/mWTFHJFwmphv7G4Zh1AGayJGNc2rCY2POWmOL8gRdT3dOODqXr43wegmGYRgpKD0TMhM4PeamCcvBJdRYLJnLt8rA5QVxgzWlgZ5hGEZFwWJgMTAMo8pBO4mNYw5NSFsHRKHS0SFm74SkofaMOUtCwzCMqoH6+LDYDFXEmglQvFUtYAU22CWXX4GN+wCXT21jGIZRsWDlsZEJWV5SbaDLMVOouTBHzB0SshjPjjGnS2gYhlGRsBhMCouBYRhVgZkS4hY6PzdxvQH37pkIguWQAPMpuYl1CfOmtjEMwyhbLB3zyoTH5PK59erjY9QOAslULcM7c+6EahhGGYIiKgLBcLeY43MTO3oSMDUaBrnOFsjlq7DJOoKIaTW71AzDKBNYDJoHFgPDMMoWNJYjNZIgKKSAjFiBURoQVtZIgLjbKFRjIZ/JuZiPYRhGnWCUygIzkGyYsTF7JEQcjObFKrn8Pd4v4cI59zcyDKOV0S5m95hHJ6TNQjVUELc2EN7DE3LPycyaIaFhGMZkh8WgdWAxMAyjTUBuoT4xT465U8JqaifR2sAFBzfI5dt9H5BwofRGhmEYLQWygk5IODjmUjlXELc2Oufy1dwQYWCFNRbQ8SI6hmE0K2ZOuE/M02JulbASFp6pFCidl3Yfw2MOTMhKa4ZhGM0Ci0Hbh8XAMIwWxXIxz0l4ZMxFc/nAMTTaHkgz5Tvql5A0VLfFNgyjSZC/mTV7b4q5WUJmB0Z5QNlF3XL5CmYFmFln2jAMo04QBO4U88KEVBHjZnBjufIF3+lcuXwnVDgu5jzJ3x30NwyjVlgMKg8WA8MwGoR0Y7nNc/mWydsmdFygcsD3DAkw0zyQBXSg1102DCMsSL9sLr/OALwgl58ZGJUNqsTPSnhSLh9wVhGbYRhVhNkSbhnz7Jh9E7qdQfWAQDJkAR3cgdsldCqqYVQRLAaGxcAwqhj4jGmBPCghxUnkoMufbFQnVspNbDFyVC7vOmQhIi9GZBgVBlUQUzdAYzkazMGO6Y2MqoZmi71z+ThCz4RenMgwKgSM8oYmpM30ijk3MTOKgxTi1XP5anNIi2wa4RmGUeawGBiNgcXAMCoIShMkIDgmNzGnnDUIDKM+UIw2R0LqTUg53j5h+9R2hmG0Ycwb88yELEhPDjk/YP+IjaaAGeQKMc9IsUONLQzDaHNYK+a9MXsldGM5ozlAptl/ExJgpoJ5jYTOQjOMNgiLgdESsBgYRhsHwb75cvl0UXhNLt+UzDBaEkvm8m2x4XG5vNvIzQwNoxUwY8I1Y16Wm7j+7fTpjQyjBaFn8NBcvsNt94SuYjeMyQCyPBiVyfjzIyRV1DBaExvGHJVwv1y+2aFbZBtGC8JiYLRFWAwMYzJBwbtNc/kFSvondFMxo61g3oSDYx6by6+bAL3MpmE0E5gJDEhIkJg4gSuIjbYKFkTaKpfvbwQPijl3jS0Mw2gwVCRGi2kKx9Riev70RobRRoF7iGJH2C+Xn82uk9Cr5xlGI2AxMMoZFgPDaAZQN0DuNmSa3TU3cSESwyg3sLb2JjFHJGQdDf5mGEYtoIoTMnIaF3P3hAiDYZQ7WCRnkYRkwY2NuVxCwzAS0DKC7At4ecxlcm4sZ1QumOGSinpdwn1zXlHNMAIsBkY1wWJgGCkQRIOsP3xzzIEJqSUwjEoHLlHW1oDEESieXDChhaEtYOqpp552yimnXBjm8qsbmc1P6gYOT/hyLr/ObHYbswROMcUUC8Opppqq2Xo1xfubFebyfu9JjmmWRJIlnklIV9Ts+2YzMv5dYN/rRrxRl06dOk2Aa6yxRmSa5cjOnTv/BuPneZvsM95UxAOk4bBLly5/Zo9nmuXEWWaZ5efs8z0JLAZmJdBiYJrF2SAxiB/2VQYPHvwXjBqAH3/8MXrxxRcDX3vttei7776L/vjjj8Bi+OuvvwI/+OCD8LlvvvkmsDXx999/B37++efRO++8Mwl/+OGHwKaA/b7//vuBn376afbtFsVXX30Vff/99zX+9vvvv0dvv/124AsvvBB98cUX0S+//BJYH9jXyy+/HL377ruBfI9tERdccMHfMBYD1n1uFsS/jbNg/Jz/kz2eYZQT1lxzzT+zz/ckaIwYYOQuvPDC6Iorrgi85ZZbopEjR9Zr3F9//fXAI444Iho0aFB07bXXBmKc6hKRloQE6plnnom233776LTTTgu88847o9NPPz267777ApuCn3/+OTr22GMDR4wYkX27RTF27Nggumk8/vjj0TnnnBN42223RRdddFH08MMPBxaDxOKMM86Ihg4dGh155JGBCNzHH3+c3bzVYTEwjOJodjFgFN21a9cwuoSMGk888cTok08+CawN//zzTxAQuNJKK0W33nprdPXVVwfGxwwzjdYExm3qqaeOjjvuuMAPP/wwuuqqq6K77747sCmYMGFCMLhw3Lhx2bdbBH/++WfgwQcfHP3666813jvggAOi4cOHB7LNDTfcUGAxvPHGG4HLLrtsdNlllxW+MwRz/Pjx2c1bHRYDwygOi0EDYDGoHRYDi4FROWh2McBQzjLLLNF+++0X+OabbwaXhPzrX3/9dXT22WdHl1xySeBTTz0VfNg77bRT4BxzzBHE4Oijjw5ccMEFg5tJhgZhIQ5x7rnnBl588cVh/3fddVfgt99+G11//fXReeedFzhmzJjgknn00UcD+Tyuj5NPPjkQQ4/B41xwlUCMYRq4PNq1axedcsopgU8++WT01ltvhWuBCCD74lwgri5cXHIzvfLKK8GtpHPGpSJXE0RY8LXr9eWXXx4NHDgwuvnmmwPx53NfEQ14/vnnB5FFUOCVV14ZXXPNNcGdBbmfnM9NN90UOGzYsHBd7733XuAJJ5xQ4/rAFltsEUQc8hn2z32VOyl9TzkH7mlsWANnm2228F3deOONgUsssUTUr1+/wnd26qmnRnfccUcQCIigcr0PPPBAIMd4+umnC+LI/eGef/TRR4G4rrgP7Ac++OCD0auvvhqNHj06kGNkxa02WAwMoziaXQwwXJtuumk0wwwzBK6yyirR7bffXjCM/ND33Xffwg9/m222CQaVOAHE+BM7OP744wPnnXfeIBiMPOECCywQPfTQQ1Hv3r0D119//SA4GsViyDbbbLPCTGOZZZYJhkfvzz///MGvjbGCOgeMWN++fQMxpmlIDLbeeuvA7bbbLsxy0gHm5ZZbLjrooIMCDzzwwGjjjTcuGLNdd901Ovzww4MQwXXWWScYsx133DFwn332CQHYbt26BTJyZx9bbbVVIPs45phjQmwBHnXUUUFQMdBw9913D+fPZyAGf+mllw7nCXfbbbdgjCUubJsFRnWmmWYK5B5x7xXn4VzXXnvtwuc32WST6N577w2xBch3dOmll0b33HNPIN8RBvz5558P5LN8txoAzD333MGgSxwQA54ZxSzWW2+9cJ26fxtssEF4XwOM6667LurVq1eIfcCePXtG999/f/aSJoHFwDCKo9nFAOA62GOPPQKnn376aPnlly8EW9daa63g+sE4QQzPSy+9VBj1MapkBoGxgwsvvHDIRmJ0DTG6GCoZ7jnnnDMYJo2KcU0hOAQ1IcaN7CQZsllnnTUYji+//DJwyJAh0ZJLLhkNGDAgnAskaJ2GxACDDjFI6QwgDOZiiy0WRuCQmUyXLl2i5557LhBBwv3CiB4uuuii4TMy1hg2Zjt8BmqGsOqqqwbyHte98847B2655ZbBOCIacOWVVw4ipM9zvdy3/v37B2JQcbVpZI+4ZsFMQCPt+eabL+rQoUPhO8DtgytIMwXS0A499NDCTIpjIQK6Xu4FoqwBAPdrtdVWC4IB+c64j5oZkCBw0kknFZIOOBZuKzKaYPyQBsHT62effTZ8T7p+ni9mG/XBYmAYxWExsBgEWAyaBouBUSlodjHApfDZZ58V0g7xZc8+++wFFwnGDf8yPnM4zzzzRI888kidYkAcAPcTxBgSZJZLYamllgp/0/sYNYyPDOFcc80VXBWkuEL827hRBIzaCiusEP30009BdGA2T15iIGOP6CAG8sHjMlp88cULbpxRo0ZFK664YiFdFhfPXnvtFR122GGBxANqEwOuS9d25plnBhcb5J526tSpsH8MO0aRfULcKPjwuXbFEjp37ly45wTocX0pZoHbLAuMsu4hcRQEDPcLxOAiRlwz7N69e9SnT586xQBXFMeFxICII+n8d9lll7A/3H2QbYi18F1AhGP//fevIQa4xgTuP64oxSh4XhpSD2ExMIziaHYxwBgQvMRgQX6k+PAVzMR/jnFRHQHGHwOjgC6jZoy/RrELLbRQMLjKhMHnjIFU8Jb8f2IAAoaUfRKEhYxCCRzLcCAG6ZG/RsIYMxXKKRgpY4bxnGaaaQp1ARhyZj8EpyExC4yvsnEQMUarGHHIDAgRkQBimKFiEIgZMQNECSIEjMY10kcoiDNwrZDXzJKYAUHEFtFRdg/3BQNNoBgS12D/iBRE+LIg1qCisd9++y3MqmSc8dFzXozIIXEN7jMiDonzcI26f8y0mAEowM0zgGjrO2eAgFhqdsb3zfcssWD2uOeeexZiBogPQXl9H1wfx5TgI9Z8B/Wh3MSAa9WgiueF+6TZFuB7VWIG95EBgeJYkwOcB+cEGYRwvtn3NUDhN8N58mzB+sBvkM9o/+wru//JDX43fA+yPdxz/tXvubH1UK19PVk0uxhg/BhN8oOHGD/cOnqoGUkSQNYP/6yzzgoPiUbdBA/JnCHACAnEMmqUGOCmwFAKGGMyUQSMDW4MRpZwww03DEFiBVuZmZANJCBEuF0IRCvojAEDOibuLUayBHohIoMR0jljiNZdd92Ca4qMI/ap9Nptt902nBMjYkgwFdHE4EFG91wDGT2Q+8IsafPNNw/EwHNduIMggXNmOxh4iMsIwZWx5ZoYTev8uB621/u1gWC6sqWeeOKJICIKADNbwG2j61OQXQFj7h0ZPTLue++9d3TIIYcUxAVwPXIz8VnccwLfP987gW5IUB0XI98T3GGHHcJsUjMXgFtJ94PniSB+fSg3MeBacWlCflM8ewyMIMBYKt2ZoD7BfAnw5ACGEJGGuH6zxpDnVs8UrlMGInINFoM6FZAhxyxarllsQkO+45YEA1GeWyWK8BtnMKZkFGxfY5At/GxtWAwsBgEWg6bBYmAxsBgUAQ8iUzxN8XFfZPP2MVbq78OUkS9fhgQfMdMxTXeZImYfsnRfHQxJ2sfP//mRaDqtvkiarrL/9OcBr6kbyP6QtA+Ml/zXaaZdYbzWlFbXofcRJX6sPDwQfzxpsrpmqDgA1DRUrzknrkHGNFu8x/mpbQdk+/R++Bv3VPegNnB8nT8PdXY7XBCKgfBe2gWgY+l+cfxszya2S7swOE4aHJ/nBvJ5Xuv74P5oGq5nAUPJdwbZV0Om3OUmBkDFmtTgENRXkJ37yHeB+xBON910NYwL94N7VMxtpPcbA/YjQZYLS4YQMc/+ThEpYj2Q9xgYKr0YsA99pzpH2Q1ckQw8FBtkQEc9TmOhAR2s7RnRMys3VPp1Fpw356ZYHO5Z4lcaaOK+5XM6nqD96btA1CCCkkZ934n20VJodjEwJkL+UUb+zC7kc2e0zr/G5EU5ioEMx5h4Bvy///2vMDtlkEPxpGpV/vWvfwXR0Ayc94jjEO+BiDMDBsXSKNDE2Gp2iQhTTKhnlBktBk61Jgg+s0AVPrJ/jqNRcm1iQAaYOmKSycc+FNcCzPwVS2RWw4BDs01iXvxOyHyDq6++eo0MNq6JWKCyDIlRETvSgIUBJ8ZZtSwYcmapirFwPH6TElf2xfskOyi2l+18wOwEpMWAe6XEE32euirI9TKL0zlAvAiaLRH3YuarQRjvkxmp2BvnyYxbXhKuMe3VaG5YDFoQCnjyBfLgPfbYY4G4YVpS4Y3aUc5igMHExUjWGsQAMlJWhprEQJX2G220UXB5ksgAcfchDiRLQIwRKby4PSAzN2asZL5BRuJ8ToaJpAhcmnK/MtPFWNYlBohOx44dAzlnjqmMNAwr7k0lNTBjxkDLEJMthqtSrzGcuCrVAgb3LxltMuZkJSJeKoRECBAjJX0we2J/ZDpC3K/cI10P9wqxwcjLfYtBrw1ZMRBweZMpSJo6JHOPZBDOAyLoCJ0Enc9j5CUeuENxiStlGtHEDSrBZx9ca0vBYmBUDcpZDDAW+NFVJY4xYhSpti0SA8V5cM1Q0yJjzLak8WKAIH57DLAMH4adqnX56Bl5L7LIIoX9ITzMJIgHQarOGbnWJQa495Qizr5JL8Y4QkbqCIRcfcS8mEFTcwQRJq5XMwmyz+LvruByQQD5m1qeIBZkxCnGgnuRe6QWMcwsMLaaGSAGxCN1fGJ4ZMGRDahr5P+1ISsGcp3h2iJWpjgKsSxiW8xyIHEzvkt1V+BvDBYlyMygOFdlDSL4iIHEhNlaS8ZNLAZG1cBiYDGwGBSHxcCoGpSzGOAqIbCPAYQUJ2LUsmKgpAMMI1XsFF1CXCuIgV7jrqTGRZ0CsmKAyyUtBhDjpoAxbpn6xIC4AokLENcoxo4+YJBzRgyUFEEWHQa6PjEQcLeki1lxGVHLku4kTJKG3F64iSjwTIsBIiggCAgKwWqdAwkutSErBkp04HpiGxlcVKoFwoDTmwuyf9zFWTHQPeU75Zgq3iRpAjFQEL6u4HJzwGLQitCIoiHVs0bpKEcxkI+bmQEGRz5ufM4gKwaM4CGGHINO0BlKDCjChIhBjx49aogBBY74vCGGl33IMHE8UqQ16kVQ0mJAanVWDDgvGXuMHj7zXXfdNZCmkRSHKgDMKJ2U67QY4B8n4AoRA3zwCpATbCbmoeJUCkoxxspSZBs68GrUzf7TYsBMBHETiJlQ8IpRloAVSxVNF3siBsoSQuwQWAWEeY/gt+I4zByYJenzFFqSYKK4Bg0c0yspIuqIgQQtm5XZ3LAYNBCotIJ1BLeoGlZePKOEphh0Ak4w/hKybxktgHITAwyF+jnxvJEto7YqjNQJwipdmfU2MLbp/k+4XTCqEANOkLR9+/aBbItbhBG9antwcWCgIN1ycS+p2y8tXqiy1zNPq3nOg0Ay5DOIVhocX510CSYTAFadAdeG6wODDJkZMDrX8TCMBHRV3YuAUM+iUTfiQuqqAtwYc2YHciOxfwLgtGqBnCOGFXcZZBSOgCkTiP3hxsEFR3Aa1jYzIPiNKEL6ruHyknhQwzPzzDOHdiqQ6nxEVR2ZESAyt9J92eiAoGvgfBFgBdWZEfE9qr0/6dstCYtBA2ExKH9YDCwGFoPisBg0AqqqZorMFFZTeH5s+B+ZukIeLNUYQF4zjVRRFX9jyqdOqvhogR5khEXbaVv9C3kvPSVXsYr2z7H0GahjFyumqRaUmxhMbvAMFWvW2BTwzMkVyu8k6/PmGZWxb8jiRFnwGaVvg6YMyNLgd8K1yxXVWHAeuKAkDrzmdyrXVH375P4QdG8tWAwagawYCPhMUXTVEfBwk42h7dXhVAU75EHjF1UhCqMmHhq1X2AER563cqgpZiH7QiMKRg3knat6kwc4fTxGeRTeqL0Go0h8lRQdZdtzVxMsBoZRHBaDRqCYGJBy99///rfGGsAE4RTco5KSbVRsgmEnoBTfz0Cmixh8ZR2wb/r/aIqLAWdKTxAMMgshoEaraUgAjaCiehExfSZ7g6k85JikqqmSsVphMTCM4rAYNAIWg/KGxcAwisNi0AgUEwOCSIiB3DoEjwh+qQcJATLEQCupsW4DbiN1nCT/mIZXBOggOdQE/JSGR8ogaX+s2wBxNZFGpz4y5FATnNMKaYgF+9PxcBXRX0YxhWqFxCB+nptNDKaYYoqzoMXAKHdYDBqBYmKA4aeARNWP5E9T7agCGGYB5GorC4HPU0SUFgMKizRzwKAzsyDjAxITQAxUfMLsAzFQjIH3yCjR8Sj2SYsBcQkjInPjbxg/0uNiHt4cjIXgUWgxMModFoNGQAU9pHupSyKk1J20PGVikJbHaF0dFiHrFShgTEobAV0Vk2CwKfrRTIKAMrMDFa9QbMRKYyr4YWbA0pKaGdDAjIIWrTyGQHA8NSVTRWa1IyUGF8bcuzkYC8H9sK2JAVltamEOmRnWBzJg1J6BLLTJDbJp0ufMs69sJKPlYTFoBCwG5Q2LQd2wGFQ3LAYNBMaaxl+Q1rf47vUaw04gV6CohcCv1hAmtRO3kJp2UYSDG0drJlNwQ8BXBUSsAUyRjNxCpInSz0UBYgLGvJbQkM5KQY5a37JvRIEWwRC3klFdMQNaGTBA0TNDIRdN0xgkwNpaqLNwi9Y70GJFaWOcfd3c4Dem3whuUtppaHU92k1k210YzQuLQQPBg6he7IycyP4hnx9mF8Hgx0L1YHqUxYxB2T+QbbQ/soXYn2IGZP4Qc2CpTciPl220vVaK47iQc0sfjyAxRS6qK2jNQpa2hGrKJuIZICNNXUIp+qJxmyp+EYsseE7VGI9nimebQQoEzDjVa6glQBGazpcBE8ensRuksRzPvdFysBi0EVCOrta5lOsz2lcHSTKPjNJRTWLAKJ6ZgVo4Uw3LLFJdQxlMMFDQ7JKZAwMIZpWQAQTrLqsRHSnJsbEoLFtJ+wdcmXQWhQgIAqTGdjR5I8lCLh+OQaGkxIRZCLNluVaF+PsJZObNgEnLfnbv3j3sU1X/zLYp3tQymZBCTa3cxvWyjc4H9y5ioqp8Zs78rpQUwj75DPsZO3ZsIL9J7qMSNXiP4k6tpsYAjM9q+VcElN+tWoLoeLrHHI/z0DW1NVgM2ggsBi0Pi4HFwGJQHBaDNgIeOrl1aHilNVSheq8YpaHaxAAjrt75GDPcRkpaIKBMYzca4EEGIRh1LaSCWBCvUu0KxgtXjZIUMOQUV6q2hpbM/J14GqRtNEs/UlMD2R8GXW4o+vSQLJHuLQQkBpwDyREq3OQcafNCMzlILIzrkOEmzsH2vXv3DqTnF3E7teRmUIXrSWsq026a89JaArimOC9igDL2XIeW2IQ0pOQztKmGrH2Ay00CydoFiJiaCSLGCJGaAdKmmhii7klLxV6aCouBUTWoNjHAyA1OqtzvuuuusG6BkhowrHTMVMAWMPKW8SRLjsCtAsoAg6y4FGsMUD/DaBwiPPj41aGTUTXioK6lnA8df9WVFDGh+2gWEoNevXqFzDsVWjKbYUah/lwIAVl2qvrnNaKkmQxrN/Tv37/QpZTzJQ6HCEJmPQgcC9hDjDOzH+4RgWvI/UMM6L4KEVTWXmC/EPFAQBFFyPUzW9I10mmUY2nGz0yC97V+QTbW2NqwGBhVg2oTA0bmchMBDBlp0BC3xZgxYwqLwwDEQG3a6xMDRvqMjBXwRUAwhnJtIgYEnjXy5nwwhBIHWrfXVg2fdROpgyizkpEjRwYRgYzSEQONyqmyJwCtbCfIyFyFoCRopMUAsUEMtBg9YkDGErModfcl44pjy5gzo0DA2C9EDHD7SAw4BgvwyE1E9wDSYxW0R5DSK51ZDAyjlWAxsBhYDIqjIsWABxn/HeQHwEOjQBWv0zUBTQFfIi2o5eMneMRr+RoJGlHAoyX9akvjqw88iEoj5SFsCrS+AgHBhhQdCdwvrcEKKwXVJAYYRoywamF4jSGS/5vfBn/HwEL89jyrCAgkWIoYKGbA84wxxf0CcXPwebVlx9gRuJUbiv3jRtIynQRX+V0qJoGQZOsGOAct7MI+MMQq7GRhGFwyMt4cn/f1GuNOGxYtMclncBfJTcTvFFeTnmkKNdlGbqITTjghfJ6aHzV0RMww8HITIaDcI7miCDpzTioWxV1GexlcclCBen0eNxHnojgIAfu2hIoUAwyZHmpINoMW1qbwhoelFDAiwC/KKAAywuDL1ULZfMlso4IZfhiNASMmfnw8nJCAWFOgCmaNahoKxE0ZJOpyyn7KHdUkBmQDUYDI8w55jogR6JllcMCIXjEDBgAMGjQzYPRPEFSjWJ5xDKZmCgRtGb0rZoDx5hiaGWBIMbKqmueZYpCk4zNazyZGMHDR6n/y9yvbB+PPwEgLQhHc5net7CJmJqzGpoAymTuch4w9hpwaHjKMII0d+ZcMJ8i1MUjEXhBohwgWgqF7wn6o+VFchIEfx1LxKO/zeQkkvzviJppJcA7EOxQzaGsDrYoUA6aIekjJOmCUo/QwHqz6VhyqD4xoGAkouMVDzA9NU2DEgB8jWUGwsYaUB4aHkGk7pLldU6BMDYJiPIgNBZ/hOjSq4n4xAip3VJMYYCgZ9Cj7B+OMm0JuF2YKGH8tuYgY8MypyAxDhQHXM8j7uIEYKUNmxwwwVHjJNjzz+rz+ppYpDG74jNw8taVW8jvS9pwzaZpKFWVWz+9Os3Ge5/TImv3xrOp8OB7nxzVDRui81uexBVyH3F68x/G1H+2Lc06ny3KPlCqKOHFuep/7xX40o8dbwKBQtofjcWxlNNlNNBlgMcjDYlATFgOLgcWgOCpSDICKXfDVMc3V9FbFJfIdkjpGmT6+QBXEEMDiYdAUmwcgDT5PMIw8bUhMAL8l/YEg4sODo8W/+fHxA5BA8XDyIOt9UuJ4WJjaQvyjBLPURwbfIwU2TFsh16VpPSSAxsOpVhdsw/H4DOQecAzlaMtlpOMhPkxrNeUGTPvl++T+IEiKibA903xN2TlXAm5tHdUkBm0N/F6IHcjHn40XGK2PihUDjYoxpl27di34DgnM8ncMGMTw4xuNr60gEPFNCX+jcAZibLPA6Kqak5EVRle9hBjVYHA1SsJ4YqzlSySwh39VMQVGQIzelelAkzrOWwFoil/YJz5RiCFmRKLiFmIS5DRrDWYKasiTVl8XxACB4FohvlQEReLEuSIW8n0iNIiB1kdAEMiMYOQH+RsjHPlSCfhZDCwGdYGROb83DdKMtoeKFQOBIBFLRSrLARcSYqAsBaZyBKwwdkopY+lJposqaGF2kAUjG2UVkI2BkVfAmpkII2aNtDHGzEq0QD0ZBxhVjg35LOeo7J/tttsujNg1hUVwCL4pmEc6G2mBEitcXwSuJR6kDjJN1spmZHogIJppkM3BtBYBhJwLgqKsB6az3CtNl9mWYBhCChELZjKaGTHTyQYD2yIsBq0HnhvPBto2LAYWA4tBCbAYNAwWg7aPihQDDJPSKkn9wg2ixeVJleR9BXFwn+DCoaBGxo4+IrhrVFZO35Us2IcCxPjTOY6MJ4vXUOij/fE+xl1NsggcUbyigh0MOIFuDDhEDNLBLVpaA8UwcOmMGDGiIFbsEwOtz+MmSgPXEu4j1V5gwAkuslYyJOaB20duKM4tKwak2gkI5m677VZI++O1xcBiYJQ3KlIMMLYylBg9jKUMKUaMGYH84xht/PoYbBlTVikjC0DGjhqC2hYDUdOtlVdeOYy4NbJn1TGCZAI+ekbgClCT14yvXsUqGH4KgRSz2HHHHUNGhTI9aIpF9ge50BDh4bxVwIPxJpCsmQHH55olRhhyRFABZ2ZBfIY4BeRYzKC0EAozBbKJFEBGQPgMQW+oY6cL+RwzsBgY5Y2KFAMaXGnVL1wYGCoFjDH0/KtgLm4R3EQYYJWuMxLHaKqAhaIZRt7FgMikp8BUbKYrfsnA4biU1EMCygR25Wbh+MwGFHDGIGP0NfOgqRZpbhI0ioQIyFFFCck+ohpUaXOIB+4ntdalwCYdUEYQMfgEkyHH5ziqLiX7icwP3TMEr0ePHoVlP5lF4RrT+VFEVA4uAIuBYRSHxcBiYDEoARYDo1JQkWJA6prWAsCIIwZyafA3XDHy32MU+Zf3tIwk2yjNE2qbYsC1lEa2mER1DXIT4fKBStXU8RXAJsiNEZdbhvMh/iE3Ep/B/aNrIq7A5+TmYnv+rgAy23NPFEfhfRUeQdxUqi8AnI/2ofPifLiXMH1/dW6OGVgMjPJGRYqBYdQGi4FhFIfFwKgaWAwMozgsBkbVwGJgGMVhMTCqBhYDwygOi4FRNbAYGEZxWAyMqoHFwDCKw2JgVA0sBoZRHA0VgxX//e9//ww7duwYmWY5csYZZ5wAYzHYOvuMNxXxb2MY7NChw5/Z45lmObF9+/Y//D8deRJtBpu3eQAAAABJRU5ErkJggg==>