# Week 0 — Billing and Architecture

For this week, I already did most of the AWS account setup like creating an admin user, securing the root account with MFA, creating a budget and alarm. So I didn't do them again. Going through the well architected tool, it was a bit difficult to follow, but i got a few bits here and there. Will go over it a few more times to fully grasp the concept as well as the different pillars.


I tried my hands out with the CI/CD architectural diagram for the project architecture on lucid chart. Here's the [link](https://lucid.app/lucidchart/176953bd-8d80-4e31-8e2a-e27759739e45/edit?viewport_loc=-635%2C-271%2C2835%2C1380%2C0_0&invitationId=inv_8f848d63-39ca-44b8-bbb2-008fe55da41d)  to it.

From my research on service limits, they refers to the max quota of resource available for use by any aws account. All the services on aws have a defined service limit that when reached, the account would be unable to further utilize any more of that particular service. Also, a request can be put in to increase the service limit of a service, to enable the account use more than the general max resource of the service.

As for putting in a request for increasing the service limit of a service, I went through the process of selecting the service I'd like to increase, but I didn't complete it. As I did not have a need to increase any service yet. But I'm sure I understand the process and would be able to go through with it, when the need arise.