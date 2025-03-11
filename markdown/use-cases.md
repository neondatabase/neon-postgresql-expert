# The Postgres API for Agents

---
title: 'The Postgres API for Agents'
subtitle: Join Replit Agent and Create.xyz and let your agent deploy Neon databases with no friction for the user.
enableTableOfContents: true
updatedOn: '2024-10-09T09:00:00.000Z'
image: '/images/social-previews/use-cases/ai-agents.jpg'
---

<Admonition type="note" title="TL;DR">
Replit Agent and Create.xyz have deeply integrated Neon into their agentic experience. The apps their agents build come with a Postgres database powered by Neon—without requiring the end-user to sign up with an external third party. If you're looking to build something similar, reach out to us.
</Admonition>

<Testimonial
text="The speed of provisioning and serverless scale-to-zero of Neon is critical for us. We can serve users iterating on quick ideas efficiently while also supporting them as they scale, without making them think about database setup."
author={{
  name: 'Dhruv Amin',
  company: 'Co-founder at Create.xyz',
}}
/>

---

AI agents can now provision infrastructure, including databases. With AI Agents already spinning up databases every few seconds, chances are they’re going to manage a big part of the web’s infrastructure in the future—and, just like developers, AI agents love working with Neon.

## Neon is ideally suited to AI Agents. Here’s why:

---

### One-second provision times.

If you’re a dev writing code, a five-minute deploy isn’t a big deal. But AI Agents generate the same code in seconds, waiting five minutes for a deployment is painful. This gets even more painful at scale.

[Neon](/) takes the world's most loved database (Postgres) and delivers it as a [serverless platform](/docs/introduction/serverless). This means that spinning up new Neon databases takes seconds vs minutes in other Postgres services.

### With scale to zero, empty databases are very, very cheap.

Imagine spinning up a new RDS instance every few seconds—you’d blow your budget on the first invoice. In most managed databases, managing thousands of isolated instances is unthinkable, and even more so without breaking the bank.

Neon’s serverless architecture solves this. In Neon, databases [automatically scale to zero](/docs/introduction/scale-to-zero) when idle and wake up instantly. You don’t pay for a database unless it’s being used or has data on it.

Some databases created by agents might only be used for a few minutes; if you’re the company behind the agent, you’ll quickly have a large database fleet full of inactive databases.

With Neon, that’s not a problem. You can still maintain this fleet within a reasonable budget.

### Straightforward API that even an AI Agent can use.

The same API endpoints that are useful for [developers managing large database fleets on Neon](/blog/how-retool-uses-retool-and-the-neon-api-to-manage-300k-postgres-databases) are also perfect for AI Agents.
Just like developers appreciate a simple, clear API, so do AI agents. If it’s easy enough for a junior dev, it’s great for AI. Neon checks that box.

With the Neon API, you can not only create and delete databases but also track usage, limit resources, and handle configuration.

### Neon is 100% Postgres

The most-loved database by developers worldwide is also the best choice for AI agents, thanks to its versatility (it works for almost any app) and the vast amount of resources, examples, and training datasets available.

Neon is simply Postgres. Everything an agent knows about Postgres is available in Neon, from extensions to full SQL syntax.

## AI agents are now provisioning more databases on Neon than humans—many thousands per day.

---

The scale is massive, and Neon is built to handle it.

### Purpose-built interfaces for AI Agents.

Neon offers dedicated interfaces that make it easy for AI agents to deploy and manage databases:

**[Model Context Protocol (MCP) server](https://github.com/neondatabase-labs/mcp-server-neon):** Enables any MCP Client to interact with Neon's API using natural language. AI agents can use Neon's MCP server to automate tasks such as creating databases, running SQL queries, and managing database migrations. [Explore our MCP guides](https://neon.tech/blog?query=MCP).

**[@neondatabase/toolkit](https://github.com/neondatabase/toolkit):** A lightweight client designed for AI agents that need to spin up Postgres databases in seconds and run SQL queries. It includes both the Neon TypeScript SDK and the Neon Serverless Driver.

```jsx showLineNumbers
import { NeonToolkit } from "@neondatabase/toolkit";

const toolkit = new NeonToolkit(process.env.NEON_API_KEY!);
const project = await toolkit.createProject();

await toolkit.sql(
  project,
  `
    CREATE TABLE IF NOT EXISTS
      users (
          id UUID PRIMARY KEY,
          name VARCHAR(255) NOT NULL
      );
  `,
);
await toolkit.sql(
  project,
  `INSERT INTO users (id, name) VALUES (gen_random_uuid(), 'Sam Smith')`,
);

console.log(await toolkit.sql(project, `SELECT name FROM users`));

await toolkit.deleteProject(project);

```

### Control resource consumption at scale.

Managing thousands of databases requires predictable resource allocation. With Neon’s API, you can:

- Set limits on compute uptime, CPU usage, data writes, storage, and data transfer
- Define different quota tiers (e.g. for free, pro, and enterprise plans)

### Define compute configuration.

AI agents need flexibility in how they allocate and scale database resources. Neon enables precise compute management:

- Configure autoscaling limits to control min/max CPU allocation
- Adjust scale to zero behavior

### Monitor the fleet.

Tracking thousands of databases requires visibility:

- Monitor total compute uptime, CPU seconds used, and data written/transferred
- Notify users before they hit hard limits

<CTA title="Next Steps" description="Meet with our team to explore possibilities for your own project." buttonText="Book time with us" buttonUrl="https://neon.tech/contact-sales" />


# Database Per User at Scale

---
title: 'Database Per User at Scale'
subtitle: Manage thousands of Postgres databases with minimal effort and costs.
enableTableOfContents: true
updatedOn: '2024-08-23T09:00:00.000Z'
image: '/images/social-previews/use-cases/db-per-tenant.jpg'
---

<Video
sources={[
{
src: "/videos/pages/doc/db-per-user.mp4",
type: "video/mp4",
},
{
src: "/videos/pages/doc/db-per-user.webm",
type: "video/webm",
}
]}
width={768}
height={432}
/>

<Admonition type="note" title="TL;DR">
Companies are managing fleets of thousands of Neon databases with very small teams and budgets. This is why:

1. **API-first**: Devs can provision databases, set usage quotas, and manage costs with ease through Neon's API.
2. **Instant provisioning**: Databases are ready in under a second.
3. **Autoscaling w/ scale-to-zero**: Neon databases pause automatically to eliminate fixed costs, and CPU/memory scale up and down automatically per-customer.

In Neon, **1 tenant = 1 project**. Our pricing plans include thousands of projects — follow this guide](https://neon.tech/docs/use-cases/database-per-user) to get started.
</Admonition>

<CTA title="Get $100 in credits" description="Sign up today and get $100 in credits when you upgrade." buttonText="Claim offer" buttonUrl="https://fyi.neon.tech/credits" />

<Testimonial
text="We’ve been able to automate virtually all database management tasks via the Neon API. We manage +300,000 projects with minimal engineering overhead"
author={{
  name: 'Himanshu Bandoth',
  company: 'Software Engineer at Retool',
}}
/>

## Why database-per-user?

One of the first design decisions you’ll face when building an application with Postgres is how to organize your multitenancy. For certain use cases, adopting a database-per-user approach is the most beneficial. Consider the following scenarios:

- **Offering a managed database to end users**: If you’re building a developer platform, low-code/no-code platform, or backend-as-a-service, you may want to provide each end user with a dedicated database, complete with a unique URL. This ensures that users have their own isolated database environment.
- **Meeting strict data privacy requirements**: If you’re operating a B2B SaaS platform with customers in regulated industries, they may require maximum data isolation at the instance level. A database-per-user approach allows you to meet these stringent data privacy demands by offering each customer their own isolated database.
- **Complying with regional data regulations**: In cases where data regulations require customer data to be stored within specific regions, creating separate databases in each region provides a straightforward path to compliance.

## Scaling database-per-user architectures in AWS is not a good idea

Scaling database per tenant architectures in managed Postgres solutions (e.g. Amazon RDS) is hard. If you fit thousands of databases inside a single RDS instance, this instance becomes a single point of failure, and it gets slow and hard to maintain. If you try to manage thousands of small instances in AWS, you start needing a dedicated DevOps team to handle the logistics. Plus, costs skyrocket.

<Testimonial
text="Our customers require their data to live in an isolated database, but implementing this in RDS was cumbersome and expensive"
author={{
  name: 'Joey Teunissen',
  company: 'CTO at Opusflow',
}}
/>

## Database-per-user in Neon

Neon is Postgres with serverless architecture. With rapid provisioning, scale-to-zero, and robust API support, you can scale database-per-user architectures without management overhead or big budgets. Just create **one project per customer** via the Neon API.

![Database-per-user](/use-cases/database-per-user.jpg)

### One project per customer

A Neon project is the logical equivalent of an "instance" but without the management heaviness:

- By creating one project per customer, each customer's data will be completely isolated.
- You'll be able to run independent PITRs without affecting your entire fleet.
- You can create different projects in different regions to match your customers' locations.

Management is simplified vs other Postgres services because,

- There’s no need to provision infrastructure in advance.
- You can scale your architecture progressively, from a few tenants to hundreds of thousands, without breaking the bank — our pricing plans include a generous number of projects within the monthly fee.
- New projects are ready in milliseconds, and you can manage everything programmatically via the API.
- You only pay for the projects that are active thanks to scale-to-zero.

<Admonition type="note" title="Tip">
You can also migrate schemas across thousands of projects [automatically.](https://neon.tech/blog/migrating-schemas)
</Admonition>

### A dedicated project for dev/test

To take advantage of [database branching workflows for dev/test](https://neon.tech/use-cases/dev-test) whithin a project-per-tenant design, create a **separate Neon project as your single non-prod environment**. The methodology:

- Load your testing data to the main branch. This main branch acts as the primary source for all dev/test environments (they can be hundreds).
- To instantly create ephemeral environments, derive child branches from the main branch. These branches are fully isolated resource-wise and already include an up-to-date copy of the testing dataset. They can then be synced with the main branch with just one click.
- Once the work is complete, ephemeral dev/test environments (child branches) can be deleted automatically via your CI/CD.

![A dedicated project for dev/test](/use-cases/dev-test.jpg)

<Admonition type="note" title="Tip">
Check the [Database Per User Guide](https://neon.tech/use-cases/database-per-tenant) in our documentation for step by step instructions on how to set this up. 
</Admonition>

## Neon for B2B SaaS: Data isolation with easy scalability

If you’re building a B2B SaaS platform, a database-per-tenant design can simplify your architecture while preserving scalability. With Neon, when you place its tenant on its own project, you offer complete data privacy to your customers via instance-level isolation. This approach also makes it easy to comply with data regulations across different regions, as projects can be created in specific locations to meet local requirements.

Each tenant can be scaled independently, optimizing both performance and costs while reducing operational risk. And in the event of an issue or a customer request, you can [run point-in-time recovery (PITR) instantaneously for a specific tenant, without impacting the rest of the fleet](https://neon.tech/docs/guides/branch-restore).

## Neon for dev platforms: Join Vercel, Replit, Koyeb, and others

If you’re instead building a developer platform including a backend, or an [AI Agent](https://neon.tech/use-cases/ai-agents), you can start offering Neon databases to your users by becoming a [Partner](https://neon.tech/partners). Neon is a cost-effective solution that can support your hobby plan and Enterprise customers at the same time. Companies like [Vercel](https://neon.tech/blog/neon-postgres-on-vercel), [Replit](https://neon.tech/blog/neon-replit-integration), and [Koyeb](https://www.koyeb.com/blog/serverless-postgres-public-preview) are already using Neon to offer Postgres to their end-users.

<Testimonial
text="Neon's serverless philosophy is aligned with our vision (no infrastructure to manage, no servers to provision, no database cluster to maintain) making them the obvious partner to power our serverless Postgres offering"
author={{
  name: 'Édouard Bonlieu',
  company: 'co-founder and CPO at Koyeb',
}}
/>

<CTA title="Next Steps" description="Sign up to Neon and get $100 in credits when you upgrade." buttonText="Claim offer" buttonUrl="https://fyi.neon.tech/credits" />


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
Try this workflow in Neon right away. You can follow the steps [in this guide](https://neon.tech/docs/use-cases/dev-test) to set things up.
</Admonition>

<CTA title="Get $100 in credits" description="Sign up now and get $100 in credits when you upgrade." buttonText="Claim the offer" buttonUrl="https://fyi.neon.tech/credits" />

## Ephemeral Environments Are Inefficient in Traditional Postgres

---

<TestimonialsWrapper>

<Testimonial
className="!mt-0"
text="Getting realistic data into our verification environments was largely unfeasible, it was time-consuming, expensive, and a beast to maintain. You need to process hefty backups, transfer costs stack up, and there’s a lot of manual oversight required just to move that data."
author={{
  name: 'Jonathan Reyes',
  company: 'Principal Engineer at Dispatch',
}}
url="/blog/how-dispatch-speeds-up-development-with-neon-while-keeping-workloads-on-aurora"
/>

<Testimonial
className="!mt-0"
text="When we were using RDS, we had trouble keeping the same environment on my computer, my developer’s environment, and production."
author={{
  name: 'Léonard Henriquez',
  company: 'Co-founder and CTO, Topo.io',
}}
url="/blog/why-topo-io-switched-from-amazon-rds-to-neon"
/>

<Testimonial
className="!mt-0"
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
2. **Sync testing data to the main branch**. Load data from your staging database / testing data into the main branch within the Neon project. This main branch acts as the primary source for all dev/test environments, and it's the only place you need to update with new data or schema changes.
3. **Creating ephemeral environments as child branches**. To instantly create ephemeral environments, derive child branches from the main branch. These branches are fully isolated resource-wise and provide you a full copy of the testing dataset. They can then be synced with the main branch with just one click, ensuring they always have the latest data while saving you the work of loading testing datasets to every single environment.
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

Yes. Overprovisioning is a big problem—we see this daily while talking to customers. If you suspect this is you, Neon can help: [autoscaling](/docs/introduction/autoscaling) is a powerful weapon against overprovisioning and the unnecessarily high costs it causes for production databases. [Read more about it here](/blog/neon-autoscaling-is-generally-available#why-autoscaling), and don’t hesitate to ask us about the migration assistance we offer. **We not only help you move production safely but also waive all migration-related fees.**

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
- **2. Explore our guide in docs.** [Follow these steps](https://neon.tech/docs/use-cases/dev-test) help you get started.

---

<Admonition type="note" title="Get $100 in credits">
Neon offers a Free Plan, and we’ll give you $100 in credits when you first upgrade. Claim the offer by signing up through [this link](https://fyi.neon.tech/credits).
</Admonition>

---

<CTA title="Got Questions? Reach out" description="There's no one size fits all with ephemeral environments - but we’re here to help you set things up. We can also discuss pricing options, annual contracts, and migration assistance." buttonText="Book a meeting with a Solutions Engineer" buttonUrl="/contact-sales" buttonClassName="xs:text-xs xs:whitespace-normal" theme="column" />


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
: - [Read how others do it](https://neon.tech/blog/from-days-to-minutes-how-neo-tax-accelerated-their-development-lifecycle)

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

[Learn how to build this](/docs/use-cases/database-per-user)

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
: Paid plans start at $19, with compute and storage resources already included. [Review our pricing plans](https://neon.tech/pricing).

Pay via AWS/Azure Marketplace
: You can subscribe to Neon via the marketplaces to consolidate billing. Click [here](https://aws.amazon.com/marketplace/pp/prodview-fgeh3a7yeuzh6?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) for AWS, and [here](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/neon1722366567200.neon_serverless_postgres_azure_prod?tab=PlansAndPrice) for Azure.

</DefinitionList>

<CTA title="Next Steps" description="Start in our Free Plan and get $100 in credits when you upgrade." buttonText="Claim offer" buttonUrl="https://fyi.neon.tech/credits" />


