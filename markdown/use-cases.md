# Neon for AI Agent Platforms

---
title: 'Neon for AI Agent Platforms'
subtitle: The battle-tested solution for agents that need backends.
enableTableOfContents: true
updatedOn: '2025-07-26T09:00:00.000Z'
image: '/images/social-previews/use-cases/ai-agents.jpg'
---

<ProgramForm type="agent" focus={true} />

If you're building agents that generate apps from prompts, your users want to build apps, not manage databases. Industry-leading platforms like Replit and V0 create databases on Neon because it aligns with how agents work: Instant, branchable, serverless Postgres data layer, invisible to users.

<Admonition type="tip" title="LLM Credits">Qualified startups can get credits towards the latest OpenAI, Llama, Claude models through the Databricks Startup program. (Neon is a Databricks Company.)</Admonition>

**Neon Features for Agents:**

- **Instant Provisioning:** your users never wait for infrastructure.
- **Snapshots:** let users toggle between checkpoints of code and state together.
- **Low cost-per-Database:** automatic scale to zero and 350ms cold starts.
- **Full-Stack, Batteries-Included:** Neon Auth, Data API included at no added charge.
- **Granular API Controls:** Track and control usage for flexible limits and invoicing.

<LogosSection containerClassName='py-3' logos={[
'anything',
'replit',
'same',
'solar',
'databutton',
]} />

<QuoteBlock quote="The speed of provisioning and serverless scale-to-zero of Neon is critical for us. We can serve users iterating on quick ideas efficiently while also supporting them as they scale, without making them think about database setup." author="dhruv-amin" role="Co-founder at Anything" />

## Agent Plan Pricing

|                            | Agent Plan                                                                                            |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| Projects                   | **Custom limits available** <br/> _Agents create a new project for each user application._            |
| Branches per Project       | **Custom limits available** <br/> _Agents use branches to quickly toggle between application states._ |
| Compute                    | from **$0.14 per CU-hour** <br/> _Same as Launch_                                                     |
| Storage                    | **$0.35 per GB-month** <br/> _Same as Launch/Scale_                                                   |
| Instant Restore (PITR)     | **$0.2 per GB-month** <br/> _Same as Launch/Scale_                                                    |
| Neon Auth                  | **Included** <br/> _All-in-one API for handling user signup and management in Neon_                   |
| Management API             | **Higher Rate Limits Available** <br/> _API for instant provisioning and management of databases_     |
| Data API (PostgREST)       | **Higher Rate Limits Available**                                                                      |
| Support                    | **Shared Slack Channel**                                                                              |
| <br/>**Agent Incentives**  |                                                                                                       |
| **LLM Token Credits**      | Access to Databricks Startup Credits for Foundation Model Serving tokens.                             |
| **Your Free Tier is Free** | Neon pays for up to 30,000 projects/month used in your free tier.                                     |
| **General Use Credits**    | Up to $30K in credits for those not eligible for the [Startup Program](/startups).                    |
| **Co-Marketing**           | Blog and Social promotions, hackathons and more.                                                      |

<QuoteBlock quote="Integrating Neon was a no-brainer. It gives every Databutton app a production-grade Postgres database in seconds, with zero overhead. Our AI agent can now create, manage, and debug the entire stack, not just code." author="martin-skow-røed" role="CTO and co-founder of Databutton" />

## How It Works

<FeatureList icons={['agent', 'speedometer', 'branching', 'database', 'lock', 'scale', 'api']}>

### Agent creates an app

A vibe coder imagines an app. Your agent builds it, full-stack. Real apps need databases, not just UI scaffolds or code snippets. Neon lets your agent add a fully functional Postgres database to every app it builds. Whether they're prototyping, testing, or deploying, your users get persistence out of the box.

### Gets a working database instantly, with no friction

Neon provisions the database behind the scenes via API, so your user never has to leave your flow or sign up for an external service. Provisioning is instant, invisible, and integrated. Your agent simply requests a project, and Neon returns a live Postgres instance. The result is a seamless experience where databases just show up, and the vibe never breaks.

### Agent adds auth

Neon makes it easy to add secure, production-ready authentication and access control to agent-generated apps using Neon Auth. Your users don't have to wire it up themselves – auth just works, right out of the box. One less thing to worry about, and one more reason their app feels real.

### Infra stays affordable as more apps are created

Imagine spinning up a new RDS instance every few seconds: you'd blow your budget on the first invoice. Most managed databases aren't built to support thousands of isolated instances, especially not cheaply. Neon's serverless architecture solves this. Databases automatically scale to zero when idle and wake up instantly. You don't pay unless the database is active or stores data.

### Branching unlocks time travel + safety

Neon branching makes it easy to build full-version history into your platform. Your agent can snapshot schema and data at any moment, and vibe coders can roll back to a working version of their app, preview earlier states, or safely test changes.

### Stay in control with quotas

The Neon API allows you to track usage per project and branch with detailed endpoints for compute time, storage, and network I/O. You can enforce quotas via the API to match your free or paid plans, giving you full control over how resources are consumed.

### It's all just Postgres

The most-loved database by developers is also the most practical choice for agents. Postgres is flexible, powerful, and battle-tested. Neon is simply Postgres: with all the extensions, full SQL syntax, and everything your agent already understands.

</FeatureList>

## Documentation

For documentation on using the Neon API to provision and manage backends on behalf of your users, see [Neon for Platforms Documentation](https://neon.com/docs/guides/platform-integration-intro).

<QuoteBlock quote="The combination of flexible resource limits and nearly instant database provisioning made Neon a no-brainer." author="lincoln-bergeson" role="Infrastructure Engineer at Replit" />

To get started with the Agent Plan [fill out the application form at the top of this page](#agent-form).


# Data Isolation at Scale

---
title: 'Data Isolation at Scale'
subtitle: Give every tenant a dedicated Postgres database. Meet compliance requirements, eliminate noisy neighbors, and scale without friction.
enableTableOfContents: true
updatedOn: '2024-08-23T09:00:00.000Z'
image: '/images/social-previews/use-cases/db-per-tenant.jpg'
---

<Admonition type="note" title="Summary">
Neon makes it easy to isolate each tenant in their own Postgres database with instance-level isolation, without the cost or complexity this architecture requires on other services (like AWS RDS).

- **No more noisy neighbors** - Every customer runs on a separate Neon project, ensuring stable performance and reducing cross-tenant risk.
- **Simplified compliance** - Meet strict data privacy and residency requirements with per-tenant isolation and regional project placement.
- **Scale each tenant independently** - Neon autoscales compute and storage per customer, without over-provisioning—and scales you down, too.
- **Instant per-customer recovery** - If there’s an issue (or a customer request), you can instantly roll back any tenant’s database without affecting the rest of your fleet.
- **API-first management** - Provision, scale, and manage all your Neon projects programmatically—one engineer can manage thousands of tenants.

Sign up [using this link](http://fyi.neon.tech/credits) to claim $100 off your first invoice, and follow this guide to get started.
</Admonition>

## Why database-per-user?

One of the first design decisions you’ll face when building an application with Postgres is how to organize your multitenancy. For certain use cases, adopting a database-per-tenant approach is the most beneficial:

- **Meet strict data privacy requirements** - If you’re operating a B2B SaaS platform with customers in regulated industries, they may require maximum data isolation at the instance level. A database-per-tenant approach allows you to meet these stringent data privacy demands by offering each customer their own isolated database.
- **Comply with regional data regulations** - In cases where data regulations require customer data to be stored within specific regions, creating separate databases in each region provides a straightforward path to compliance.
- **Simplify management** - If your customers require isolated workflows like backups, PITR, or migrations, database-per-tenant makes these easier to manage without cross-tenant risk.
- **Avoiding noisy neighbors** - When customers share an instance, a spike in usage from one tenant can degrade performance for others. Isolating tenants ensures consistent performance.

![Postgres instance per tenant](/use-cases/multitenant-postgres-instance-per-tenant.jpg)

## Scaling database-per-user architectures in AWS is not a good idea

Managed Postgres services like Amazon RDS weren’t designed for high-volume, database-per-tenant use cases. While you can technically isolate each customer with their own database, doing so at scale becomes operationally and financially unsustainable.
There are two common paths teams take—both with major drawbacks:

### 1. Cramming thousands of databases into a single RDS instance

Many teams try to save money by putting all their tenants into one large RDS instance. But this leads to:

- **Single point of failure** - If that instance goes down, all of your customers are impacted.
- **Noisy neighbors** - Resource-hungry tenants can degrade performance for others sharing the same compute.
- **Complex maintenance** - Backups, PITR, monitoring, and upgrades become harder to manage when they're tied to a massive shared instance.
- **Rigid scaling** - You can’t scale individual tenants—you have to scale the entire instance, often overpaying for idle capacity.

![Multi-tenant Postgres instance for all tenants](/use-cases/multitenant-single-postgres-instance.jpg)

### 2. Spinning up one RDS instance per tenant

This approach gives you the isolation you’re looking for, but it comes at a steep cost—both in dollars and engineering time. The truth is, RDS was never designed for this kind of architecture:

- **Expensive and wasteful** - Each RDS instance has a baseline cost, even when idle. Multiply that across hundreds or thousands of tenants, and your bill quickly becomes unsustainable. Storage also doesn’t scale down: once it grows, you’re stuck paying for it.
- **No dynamic scaling** - RDS instances don’t autoscale. Resizing compute often requires manual intervention—and in many cases, downtime.
- **High operational burden** - You’ll soon need a dedicated team just to handle instance provisioning, monitoring, patching, and scaling logistics. Even basic tasks become complex at scale.
- **Slow setups** - Spinning up a new RDS instance can take minutes, not seconds—far from ideal from the end-user experience.

<Testimonial
text="Our customers require their data to live in an isolated database, but implementing this in RDS was cumbersome and expensive"
author={{
  name: 'Joey Teunissen',
  company: 'CTO at Opusflow',
}}
/>

## Postgres the way multi-tenant SaaS was meant to work

Neon reimagines Postgres for modern SaaS. With serverless infrastructure, autoscaling, and scale-to-zero, Neon eliminates the overhead that typically makes database-per-tenant architectures so hard to manage. Each customer lives in their own isolated project, and everything—from provisioning to recovery—is API-driven. You get true instance-level isolation without the cost or complexity of managing thousands of traditional Postgres instances.

### One project per customer

**A Neon project is the logical equivalent of an "instance", but without the operational heaviness.**

- Each customer's data is completely isolated
- You can run independent PITRs for a single tenant without affecting your entire fleet
- You can deploy projects in specific regions to meet local compliance requirements
- You avoid noisy neighbors entirely—no resource contention between tenants

![Database-per-user](/use-cases/database-per-user.jpg)

### Scale each tenant independently

In RDS, you’d have to choose an instance size and disk allocation up front—and scale manually as usage changes. With Neon, compute autoscales on demand, and storage grows and shrinks automatically. **You don’t need to provision compute or storage in advance.** Every tenant gets their own resources, and those resources scale automatically based on usage. No manual resizing, no idle waste.

- **No more over-provisioning** - Your busiest customers get more power when they need it. Everyone else runs lean—or not at all.
- **Scale to zero when idle** - If a tenant isn’t using their database, Neon pauses compute and you pay nothing until they return.
- **Fine-grained control** - Set compute limits, quotas, and performance policies per tenant to match their plan or use case.

<Admonition type="note" title="info">
Keep reading about how [compute autoscaling](/docs/introduction/autoscaling) works in Neon.
</Admonition>

### Rollback a single customer in seconds

In most managed Postgres services like RDS, restoring a database is a slow, manual process. It typically involves spinning up a new instance from a snapshot, waiting several minutes (or longer), and restoring all databases that lived inside that instance—whether or not they were affected.

Neon takes a completely different approach. Thanks to our copy-on-write storage engine, **Neon lets you restore databases to any previous moment instantly**—with no downtime, no data duplication, and no need to preconfigure backups.

- You can restore just one customer’s database (project) to any point in time—within seconds.
- You don’t affect other tenants, because recovery operations are fully isolated.
- You don’t have to spin up new infrastructure—recovery happens in place, with zero operational overhead.

This is especially valuable in B2B SaaS platforms, where customers may request a rollback to a specific date due to data errors, user mistakes, or compliance requirements. With Neon, you can fulfill these requests in seconds—without escalation, without disruption, and without touching the rest of your fleet.

<Admonition type="note" title="info">
Learn more about how [instant restore](/docs/introduction/branch-restore) works in Neon.
</Admonition>

### API-first management

Neon was built to help you manage thousands of Postgres databases like they’re one. Every operation—provisioning, configuring, scaling, restoring, deleting—is available via our public API. This enables you to fully automate your database lifecycle and **manage a massive tenant fleet with minimal engineering effort.**

- **Provision at scale** - Create new databases for customers programmatically, in milliseconds, with no infrastructure to manage or pre-allocate.
- **Track usage and enforce limits** - Set per-project quotas for storage, compute, and active time to align with your pricing tiers or customer plans.
- **Control costs at the tenant level** - Monitor usage and apply automated limits or alerts before tenants exceed plan thresholds.
- **Billing aligned to actual usage** - Neon’s pricing is based on consumption—not provisioned capacity—so you only pay for what each tenant uses.
- **One engineer can manage thousands of tenants** - With the right automation in place, there's no need for a large DevOps team.

<Admonition type="note" title="Info">
Explore the [Neon API documentation](/docs/reference/api-reference) and start building.
</Admonition>

### Data compliance and security

When you're building a multi-tenant SaaS platform—especially in regulated industries—data privacy and compliance aren’t optional. With Neon, instance-level isolation is built into the architecture, making it **easier to meet the strictest customer and regulatory requirements.**

- **True data isolation** - Each customer lives in their own Neon project, with completely separate compute and storage. There's no risk of cross-tenant data access or resource contention.
- **Regional project placement** - Deploy tenant data in specific geographic regions to meet data residency requirements like GDPR, HIPAA, or industry-specific regulations.
- **Access control at the project level** - Assign unique credentials and connection strings per tenant, and manage access on a per-project basis.
- **Audit-friendly recovery workflows** - Instant, per-tenant PITR enables precise rollback to any point in time—helping you meet data retention and recovery SLAs.
- **Enterprise-level security** - All Neon projects use TLS for connections, and built-in encryption is applied to data at rest and in transit.

<Admonition type="note" title="Info">
[Review our security page](/security) for details on compliance, SLAs, and our full security commitments.
</Admonition>

### Development environments

To take advantage of [database branching workflows for dev/test](/use-cases/dev-test) whithin a project-per-tenant design, create a **separate Neon project as your single non-prod environment**. The methodology:

- Load your testing data to the main branch. This main branch acts as the primary source for all dev/test environments (they can be hundreds).
- To instantly create ephemeral environments, derive child branches from the main branch. These branches are fully isolated resource-wise and already include an up-to-date copy of the testing dataset. They can then be synced with the main branch with just one click.
- Once the work is complete, ephemeral dev/test environments (child branches) can be deleted automatically via your CI/CD.

<Admonition type="note" title="Info">
Read more about [how to do dev/test environments in Neon](/use-cases/dev-test) using branches.  
</Admonition>

<CTA title="Start building" description="Sign up today and claim $100 in credits when you upgrade." buttonText="Claim offer" buttonUrl="https://fyi.neon.tech/credits" />


# Neon for Development and Testing

---
title: Neon for Development and Testing
subtitle: Boost developer productivity with Neon—a flexible development sandbox for running non-production workloads.
enableTableOfContents: true
updatedOn: '2024-08-23T09:00:00.000Z'
image: '/images/social-previews/use-cases/dev-test.jpg'
---

![Dev/Test branching](/use-cases/dev-test-branching.jpg)

<Admonition type="note" title="TL;DR">
Database branching is a game-changer for dev/test environments: there's no need to manage seed data, keep environments in sync, or wait for instances to be available. What you get: more developer velocity with +75% less costs.
- You can use Neon for your ephemeral environments even when production lives somewhere else:  
  - You keep your production DB in your current Postgres
  - You "move" your non-prod environments to Neon (i.e. by syncing a subset of data daily)
  - To build / test / debug in Neon
  - Once the changes are tested, you apply them back to prod
Try this workflow in Neon right away. You can follow the steps [in this guide](/docs/use-cases/dev-test) to set things up.
</Admonition>

<CTA title="Get $100 in credits" description="Sign up now and get $100 in credits when you upgrade." buttonText="Claim the offer" buttonUrl="https://fyi.neon.tech/credits" />

## Ephemeral Environments Are Inefficient in Traditional Postgres

---

<TestimonialsWrapper>

<Testimonial
text="Getting realistic data into our verification environments was largely unfeasible, it was time-consuming, expensive, and a beast to maintain. You need to process hefty backups, transfer costs stack up, and there’s a lot of manual oversight required just to move that data."
author={{
  name: 'Jonathan Reyes',
  company: 'Principal Engineer at Dispatch',
}}
url="/blog/how-dispatch-speeds-up-development-with-neon-while-keeping-workloads-on-aurora"
/>

<Testimonial
text="When we were using RDS, we had trouble keeping the same environment on my computer, my developer’s environment, and production."
author={{
  name: 'Léonard Henriquez',
  company: 'Co-founder and CTO, Topo.io',
}}
url="/blog/why-topo-io-switched-from-amazon-rds-to-neon"
/>

<Testimonial
text="RDS becomes a bottleneck if you don’t have full-time DevOps dedicated to it."
author={{
  name: 'Joey Teunissen',
  company: 'CTO at OpusFlow',
}}
url="/blog/how-opusflow-achieves-tenant-isolation-in-postgres-without-managing-servers"
/>

</TestimonialsWrapper>

**Provisioning instances is slow. Once they're live, you have to babysit them**. New instances have to be configured, they take a while to be available, and once running, they need constant oversight to ensure they are appropriately sized and ready.

**You pay for non-prod instances 24/7 even if you only use them for a few hours**. Production databases stay on 24/7, but this is not the case for dev/test instances. But in RDS/Aurora, unless you manually pause them, you’ll keep paying even if they're not running.

**It's hard to keep data in sync across environments**. Syncing data across many instances requires repetitive, manual work. This leads to discrepancies that compromise test reliability and slow down deployments.

**These problems get worse over time, not better**. As your number of instances grows, the manual setup and configuration work grows too.

![Persistent environments in AWS RDS](/use-cases/aws-rds-environments.jpg)

## Use Neon Branches For Your Dev/Test Workflows

---

<TestimonialsWrapper>

<Testimonial
text="Developers already face significant delays when working on a PR—running CI tests, ensuring everything is ready for preview, it all adds up. Time to launch is crucial for us: when we tried Neon and saw that spinning up a new branch takes seconds, we were blown away"
author={{
  name: 'Alex Co',
  company: 'Head of Platform Engineering at Mindvalley',
}}
url="/blog/how-mindvalley-minimizes-time-to-launch-with-neon-branches"
/>

<Testimonial
text="Neon’s branching paradigm has been great for us. It lets us create isolated environments without having to move huge amounts of data around. This has lightened the load on our ops team, now it’s effortless to spin up entire environments."
author={{
  name: 'Jonathan Reyes',
  company: 'Principal Engineer at Dispatch',
}}
url="/blog/how-dispatch-speeds-up-development-with-neon-while-keeping-workloads-on-aurora"
/>

</TestimonialsWrapper>

We get it—migrating a production database is a big project, but you can still improve your non-pod experience by moving your dev/test environments to Neon.

### Why should I move my dev databases to Neon?

Neon is a Postgres provider that offers a much more modern developer experience than databases like RDS. We’ve built a serverless platform for Postgres focused on helping you ship faster instead of being held back by database management. As the cherry on top, you’ll save money.

### Why it’s faster (and more affordable) to do dev/test in Neon?

1. **Instant provisioning**. In Neon, it takes seconds to spin up new Postgres instances. Developers can start coding and testing immediately, no waiting time.
2. **Database branching for ephemeral environments**. Neon's copy-on-write branching allows devs to create full copies of their testing dataset instantly and without consuming extra storage. This eliminates the operational load that comes with keeping testing data in sync across environments: In Neon, you can sync data with parent in one click. Branches are also extremely affordable.
3. **Non-prod environments are automatically paused when unused**. If a database branch is idle, Neon pauses it automatically to save costs (and management work).
4. **Intuitive DX with CI/CD integration**. Neon comes with a modern interface and APIs (no need to waste time navigating AWS obscurities). You can add Neon to your CI/CD pipelines to automate branch creation /deletion.

![Ephemeral environments in Neon](/use-cases/ephemeral-environments.jpg)

### How does it work?

Here's how you'll go about it:

1. **Set up a single Neon Project for dev/test**. Many non-prod instances can be substituted by a single Neon project.
2. **Sync testing data to the production branch**. Load data from your staging database / testing data into the production branch within the Neon project. This production branch acts as the primary source for all dev/test environments, and it's the only place you need to update with new data or schema changes.
3. **Creating ephemeral environments as child branches**. To instantly create ephemeral environments, derive child branches from the production branch. These branches are fully isolated resource-wise and provide you a full copy of the testing dataset. They can then be synced with the production branch with just one click, ensuring they always have the latest data while saving you the work of loading testing datasets to every single environment.
4. **Automatic branch cleanup and scale to zero**. After development or testing is complete, ephemeral branches can be deleted automatically via the API. Neon's scale to zero automatically pauses these environments when unused, so you don't have to worry too much about them.

### How much cost savings have you seen vs RDS/Aurora?

By leveraging Neon's shared storage and compute autoscaling, it’s not rare to see **customers lowering their non-production database costs by 75% or more**. You only pay for the compute you actually use—no more bloating in your bill. The same goes for data redundancies—they’re also avoided.

### Show me a real use case example

**Non-prod deployment in AWS RDS (us-east-1):**

- 10 development and test instances (db.m5.large: 2 vCPUs, 8 GB RAM) with 50 GB storage allocated in each instance
- They’re active 4 hours/day on average
- RDS monthly costs: $1,356.90
  - Compute costs: $0.178/hour \* 730 hours \* 10 instances = $1,299.40 /month
  - Storage costs: 50 GB \* $0.115 GB-month \* 10 instances = $57.50

**Equivalent non-prod deployment in Neon:**

- [Scale pricing plan](/pricing): $69 /month
- Includes 50 GB of storage - 1,000 projects - 500 branches per project
- Plus 750 compute hours, additional compute hours billed at $0.16 per CU
- **Neon monthly costs: $338.12**
  - Compute hours per branch per month: 2 CU \* 4 hours \* 30.4 days/month = 243.2
  - Total compute hours: 243.2 \* 10 branches = 2432
  - Cost of additional compute hours: [2432 - 750] \* $0.16 = $269.12 /month

In this case, migrating non-production environments from AWS RDS to Neon meant 75% cost savings.

<ComputeCalculator
className="mt-10"
databases={[
{
type: 'Dev databases',
instance: 'db.t4g.micro',
usage: 'Used interminently',
},
{
type: 'Test databases',
instance: 'db.t3.medium',
usage: 'Used interminently',
},
]}
inputParamsBlock={[
{
title: 'Deployment',
items: [
{
name: 'test_databases_num',
title: 'Number of test databases',
values: [1, 3, 5, 10],
},
{
name: 'dev_databases_num',
title: 'Number of dev databases',
values: [1, 3, 5, 10],
},
],
},
{
title: 'Usage',
items: [
{
name: 'test_databases_daily_hrs',
title: 'How many hrs/day are test databases&nbsp;running?',
values: [1, 2, 3, 5, 8],
},
{
name: 'dev_databases_daily_hrs',
title: 'How many hrs/day are dev databases&nbsp;running?',
values: [1, 2, 3, 5, 8],
},
],
},
]}
values={[
{
name: 'wasted_money',
title: 'Dollars overpaid',
valueClassName: 'bg-variable-value-1',
period: 'month',
},
{
name: 'saved_money',
title: 'Bill that could be saved',
period: 'month',
valueClassName: 'bg-variable-value-2',
text: 'With scale to zero',
},
]}
textSize="md"
/>

<CTA title="Reach out to us for an exact quote" description="Tell us more about your use case and we’ll send you back detailed information on how much you could save with Neon." buttonText="Contact us" buttonUrl="/contact-sales" />

### Can Neon also help lower the costs of my production database?

Yes. Overprovisioning is a big problem—we see this daily while talking to customers. If you suspect this is you, Neon can help: [autoscaling](/docs/introduction/autoscaling) is a powerful weapon against overprovisioning and the unnecessarily high costs it causes for production databases. [Read more about it here](/blog/neon-autoscaling-is-generally-available#why-autoscaling).\*\*

<TestimonialsWrapper>
  
<Testimonial
text="Neon worked out of the box, handling hundreds of Lambdas without any of the connection issues we saw in Aurora Serverless v2. On top of that, Neon costs us 1/6 of what we were paying with AWS."
author={{
  name: 'Cody Jenkins',
  company: 'Head of Engineering at Invenco',
}}
/>

<Testimonial
text="We had to overprovision Aurora to handle our spiky traffic, and even then, the writer database would get overwhelmed. We provision 10x more than we need on average to keep things running smoothly."
author={{
  name: 'Jonathan Reyes',
  company: 'Principal Engineer at Dispatch',
}}
url="/blog/how-dispatch-speeds-up-development-with-neon-while-keeping-workloads-on-aurora"
/>

</TestimonialsWrapper>

## Get Started in Two Steps

- **1. Create a Neon account**. Sign up for our Free Plan [here](https://console.neon.tech/signup) (no credit card required).
- **2. Explore our guide in docs.** [Follow these steps](/docs/use-cases/dev-test) help you get started.

---

<Admonition type="note" title="Get $100 in credits">
Neon offers a Free Plan, and we’ll give you $100 in credits when you first upgrade. Claim the offer by signing up through [this link](https://fyi.neon.tech/credits).
</Admonition>

---

<CTA title="Got Questions? Reach out" description="There's no one size fits all with ephemeral environments - but we're here to help you set things up. We can also discuss pricing options and annual contracts." buttonText="Book a meeting with a Solutions Engineer" buttonUrl="/contact-sales" buttonClassName="xs:text-xs xs:whitespace-normal" theme="column" />/>


# Postgres for SaaS

---
title: 'Postgres for SaaS'
subtitle: Build and scale your SaaS faster thanks to autoscaling, database branching, and the serverless operating model.
enableTableOfContents: true
updatedOn: '2024-08-23T09:00:00.000Z'
image: '/images/social-previews/use-cases/postgres-for-saas.jpg'
---

<UseCaseContext />

## Summary

Three features make Postgres on Neon a solid foundation for teams building SaaS applications:

<DefinitionList bulletType="check">
Database branching
: Create ephemeral environments with production-like copies of your data and schema for end-to-end testing, development, and previews.

Autoscaling
: CPU, Memory, and storage scale up and down to match your workload. No more manual resizes or paying for resources you don't need.

Serverless
: Never touch a `pg_hba.conf`, or SSH into anywhere. In Neon, operational work is either abstracted away or presented in an intuitive UI + API.
</DefinitionList>

**The result:**
Teams ship faster and more efficiently, with less risk of outage during times that matter most.

<Testimonial
text="In GCP, we had to constantly think about provisioning new instances and migrating data, which added operational overhead. With Neon, we can start small and scale up. We don’t have to think about some level of operational stuff. That’s awesome."
author={{
  name: 'Paul Dlug',
  company: 'CTO of Comigo.ai',
}}
/>

<CTA title="Get $100 in credits" description="Sign up now and get $100 in credits when you upgrade." buttonText="Claim offer" buttonUrl="https://fyi.neon.tech/credits" />

## Key features

---

### Database branching

A branch in Neon is a copy-on-write clone of your database. Branches include both schema and data. Teams use them to create ephemeral environments for development, testing, and preview environments.

- **Branch creation is instant** - Independent of DB size. Storage is not duplicated for each branch.
- **Branches are cost-efficient** - You can deploy thousands of branches for $19 /month.
- **Branch compute can scale to zero when idle** - to further reduce cost.

How branches can be used to increase development velocity:
<DefinitionList bulletType="check">
Onboard Faster, Keep Collaboration in Sync
: Give each developer on your team their own branch for local development. They can use [branch reset](/docs/introduction/point-in-time-restore) to instantly restore and catch up with the latest changes.

One Branch per PR
: Use automation to give each git branch or Pull Request a corresponding database branch. This can be done with automation tools like GitHub Actions, or more easily as part of an integration:
: - [Neon GitHub integration](/docs/guides/neon-github-integration) - An easier way to create a branch for every PR.
: - [Neon Vercel Integration](/docs/guides/vercel) - Create and integrate a branch into every Vercel Preview deployment.

Ephemeral Environments for Dev/Test
: Deploy confidently by using branches to run your test suite on an exact copy of your production database. No handling of seed data, no manual work keeping environments in sync.
: - [See guide in docs](/docs/use-cases/dev-test)
: - [Read how others do it](/blog/from-days-to-minutes-how-neo-tax-accelerated-their-development-lifecycle)

</DefinitionList>

---

### Autoscaling

Neon dynamically adjusts the amount of resources allocated to your database in response to the current load, eliminating the need for manual intervention.

<DefinitionList bulletType="check">
Performance w/ cost-efficiency
: Your CPU/memory automatically scale up during traffic spikes. When you no longer need the extra resources, your database scales down.

No manual resizes for compute or storage
: Other platforms require downtime for resizes, limit the frequency of resizes, and don't let you scale storage down. On Neon everything is automated and instant.

Performance for high connections  
: Neon has pbBouncer built-in at no extra cost. Use pooling and keep scaling.
</DefinitionList>

---

### Serverless

Neon abstracts away the concept of servers so that you can focus on building your SaaS, not managing your database.

- No compute/storage management: With Neon you don’t need to provision, maintain, resize, or administer servers.
- Managed infrastructure: Neon handles all underlying infrastructure, including security patches, load balancing, and capacity planning.
- Built-in availability and fault tolerance: Neon has multi-AZ storage redundancy and rapid recovery built-in.

---

## Database-per-tenant SaaS

If your SaaS project could benefit from multitenancy, Neon makes it simple to create a dedicated database for each user:

- **Instant deployment**: Neon projects are created in milliseconds via APIs.
- **No pre-provisioning**: You can scale your architecture progressively, from a few tenants to thousands.
- **Pay per usage**: You only pay for the tenants that are actively running.

[Learn how to build this](/docs/guides/multitenancy)

<Testimonial
text="The ability to spawn databases that can scale down to zero is incredibly helpful and a model fits well with our one database per customer architecture"
author={{
  name: 'Guido Marucci',
  company: 'co-founder at Cedalio',
}}
/>

## Table Stakes

### Compatibility

---

<DefinitionList bulletType="check">
It's Just Postgres
: Deploy Postgres 15, 16, and 17 on Neon. There is no lock-in and no proprietary syntax to learn.

Integrates with any language/framework
: Anything that has a Postgres driver or integration works with Neon.

70+ Postgres extensions
: `pgvector`, `postGIS`, `timescaledb` and [66 other extensions](/docs/extensions/pg-extensions) are supported on Neon

Logical Replication
: Inbound (Neon as subscriber) and outbound (Neon as publisher) logical replication supported.

Serverless (HTTP) Driver
: Unlock access from serverless environments like AWS Lambda and Cloudflare Workers with the Neon serverless driver. It uses an HTTP API to query from edge/serverless with lower latency.
</DefinitionList>

### Security and Compliance

---

<DefinitionList >

Data regulations
: Neon complies with CCPA, GDPR, ISO 27001, ISO 27701, SOC 2, SOC 3, and HIPAA.

99.95% SLA
: For Business and Enterprise customers.

Private Link, IP Allow
: To restrict access to trusted addresses.

</DefinitionList>

### Billing

---

<DefinitionList bulletType="check">
Subscription plans
: Paid plans start at $19, with compute and storage resources already included. [Review our pricing plans](/pricing).

Pay via AWS/Azure Marketplace
: You can subscribe to Neon via the marketplaces to consolidate billing. Click [here](https://aws.amazon.com/marketplace/pp/prodview-fgeh3a7yeuzh6?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) for AWS, and [here](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/neon1722366567200.neon_serverless_postgres_azure_prod?tab=PlansAndPrice) for Azure.

</DefinitionList>

<CTA title="Next Steps" description="Start in our Free Plan and get $100 in credits when you upgrade." buttonText="Claim offer" buttonUrl="https://fyi.neon.tech/credits" />


