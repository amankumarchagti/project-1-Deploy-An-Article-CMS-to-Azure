# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

Answer: I've used VM instead of App service to deploy the whole app..but I think app service is better to be used rather than VM because, in VM, we need to met certain requirements like my VM has a default version of python=3.9.2 but the requirement was python=3.7. so it took me much more time to downgrade to python 3.7. and Also in case of costs, availability, and workflow, app service is very much better and easier to operate. also, it is cost-effective as well.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 


it would be a lot easier for me to deploy the app on the app service. because to manage workflow, it will automatically create a YAML file to manage the tasks and in this way, it will create much less time to deploy.
