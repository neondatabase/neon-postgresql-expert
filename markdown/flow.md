# One branch per developer

---
title: 'One branch per developer'
subtitle: 'Eliminate developer conflicts with isolated database environments for each team member'
updatedOn: '2025-07-08T12:47:21.296Z'
---

In traditional workflows, developers often share a staging or development database, leading to conflicting changes, overwritten test data, and hard-to-reproduce bugs. With Neon, each developer can work in a fully isolated environment by branching off a shared, production-like template such as `main-dev` or `main-anon`.

For example, a developer named Arjun might create a branch called `dev-arjun`. This branch has the full schema and data of the parent but is completely isolated. Any schema changes or debugging work happen independently, without affecting anyone else.


# One branch per preview

---
title: 'One branch per preview'
subtitle: 'Automatically create isolated database environments for every pull request and preview deployment'
updatedOn: '2025-07-08T12:47:21.296Z'
---

Every time a pull request is opened, Neon can help power a full-stack preview (including a live backend and database) by creating a dedicated branch. Thanks to Neon’s integration with platforms like Vercel and Netlify, this setup is seamless and requires minimal configuration.

When you install [Neon’s Vercel integration](/docs/guides/vercel-overview), each new Vercel preview deployment automatically spins up a matching database branch named like `preview-pr-142`. The branch inherits your schema and data, and Vercel injects the `DATABASE_URL` into the preview environment. Once the PR is closed or merged, the branch can be automatically torn down, keeping your project clean and cost-efficient.Preview deployments use production-like data without manual cloning.


# One branch per test run

---
title: 'One branch per test run'
subtitle: 'Ensure reliable, isolated testing with fresh database environments for every CI/CD pipeline run'
updatedOn: '2025-07-08T12:47:21.296Z'
---

Automated testing demands clean, isolated environments. Neon lets your CI pipeline spin up a fresh database for every test suite, ensuring reliability and parallel execution. **Here’s how it typically works**:

- The CI job creates a branch named `ci-<build-id>` (e.g., `ci-20240619-abc123`)
- Your tests run in isolation against that database
- Once testing concludes, the branch is deleted or reset

This gives you complete reproducibility (every test run starts from the same baseline) and no shared state or interference between tests.


# Branches

---
title: 'Branches'
subtitle: 'Understand how Neon branches provide instant, cost-efficient database clones with copy-on-write storage'
updatedOn: '2025-07-08T12:47:21.296Z'
---

A branch in Neon is a lightweight, copy-on-write clone of your database. It inherits both the schema and data from its parent, but shares the same underlying storage. That means branches are fast to create, cost-efficient to run, and safe to discard.

<strong>Key properties of Neon branches</strong>:

- <strong>Instant creation</strong>. Branches spin up in seconds even for terabyte-scale datasets. There’s no exporting, importing, or replication setup.
- <strong>Copy-on-write storage</strong>. A new branch references its parent’s data until changes are made. Then, only the diffs are written.
- <strong>Ephemeral by design</strong>. Idle branches scale to zero automatically. You only pay for active compute and the storage you actually use.
- <strong>Resettable</strong>. Any branch can be instantly reset to match its parent. No teardown scripts. No fragile seed files.


# Branching for agents

---
title: 'Branching for agents'
subtitle: 'Enable safe AI agent workflows with database checkpoints, rollbacks, and time travel capabilities'
updatedOn: '2025-07-08T12:47:21.296Z'
---

As agents become more capable (generating code, running migrations, modifying data) the risk of unintended changes grows. For users, this creates friction and fear: _What if the agent breaks something? How do I undo it?_

Neon makes checkpointing and time travel possible in [agentic platforms](/blog/replit-app-history-powered-by-neon-branches). This architecture already powers real-world products - using branching, you can build these features behind the scenes:

- **Checkpoints with full rollback**. Agents can snapshot both code and data at each decision point. If something goes wrong - a bad migration, broken logic, or dropped table, users can rewind with one click.
- **Live previews of past states**. If a user wants to revisit a version from three days ago, they can branch the database at that timestamp, load the matching code, and preview the app exactly as it was.
- **Low-friction restores**. If an agent deploys a bad version, simply promote a previous branch to restore a known-good state, without any ad hoc scripting or manual recovery needed.


# Ephemeral environments

---
title: 'Ephemeral environments'
subtitle: 'Create disposable, serverless database environments that spin up instantly and clean up automatically'
updatedOn: '2025-07-08T12:47:21.296Z'
---

In serverless workflows, everything is meant to be disposable. With Neon, you can create short-lived Postgres environments as branches that spin up instantly and shut down automatically. Using tools like [Neon Local](/docs/local/neon-local), branches are provisioned on container start and cleaned up on exit.

Each environment is fully isolated, mirrors your schema and test data, and requires zero manual setup. You get fast and reproducible environments that feel like production but disappear when you’re done.


# Hierarchies

---
title: 'Hierarchies'
subtitle: 'Learn how to structure your database branching strategy with root branches and child environments'
updatedOn: '2025-07-08T12:47:21.296Z'
---

Every Neon project begins with a root branch: a baseline environment from which all others can be derived. By default, this is typically called `main`, but the name and purpose are entirely up to you. What matters is that this root branch serves as the anchor for the rest of your environments.

From there, you can create child branches - lightweight copies that inherit schema and data from the root, but operate independently. These branches can be reset, discarded, or promoted without affecting their parents. Think of them as safe, on-demand workspaces built from a known-good state.

In most projects, the root branch (often `main`) becomes your source of truth. It might represent your actual production environment, or a production-like clone seeded with trusted data. From this base, teams derive temporary environments for development, testing, QA, automation, and so on.

This model also makes it easy to handle sensitive data responsibly. When production contains PII or other regulated information, teams can create a schema-only branch. This is a type of branch that includes only the database structure, not the data itself.

Anonymized or synthetic data can then be loaded into this branch, creating a safe, production-like baseline for development, testing, and preview environments. It becomes a trusted intermediate layer in your branching hierarchy - one step removed from production, but still faithful to its shape and scale.


# Identifying your use case

---
title: 'Identifying your use case'
subtitle: 'Choose the right branching strategy based on your production setup, data sensitivity, and team workflow'
updatedOn: '2025-07-08T12:47:21.296Z'
---

There’s no single right way to use Neon branching. Your architecture will depend on where your production data lives, whether you need to handle PII, and how your team works.

For teams used to traditional server-based databases (managing long-lived instances, duplicating environments manually, or maintaining seed scripts) branching requires a shift in mindset. But once you experience the flexibility of on-demand, ephemeral environments, you won’t go back.

This section outlines common branching strategies based on real-world patterns. Navigate to the scenario that most resembles your use case.

![Decision tree](/images/pages/flow/decision-tree.png)


# Traditional database workflows are broken

---
title: 'Traditional database workflows are broken'
subtitle: 'Learn how outdated database practices slow down development and create bottlenecks for modern teams'
updatedOn: '2025-07-08T12:47:21.296Z'
---

Modern developer tooling has shortened software release cycles dramatically — but the database remains a bottleneck for most teams. Engineers still spend a disproportionate amount of time on tasks that should be automated or obsolete:

- **Seed file maintenance.** Keeping test data in sync across environments is painful and error-prone. Any schema change or data requirement forces manual updates and PR churn.
- **Manual environment setup.** End-to-end testing requires clean, isolated environments - but spinning up new database instances, loading schema, and importing seed data introduces costly delays.
- **Shared development databases.** When multiple developers share a single database, they run into concurrency issues, test conflicts, and overwritten data. Larger teams often end up duplicating environments just to stay productive.

These patterns slow down releases, reduce confidence in testing, and create friction between developers and operations teams.


# You’re using Neon for dev/test

---
title: 'You’re using Neon for dev/test'
subtitle: 'Adopt Neon branching gradually by starting with development and testing environments while keeping production elsewhere'
updatedOn: '2025-07-08T12:47:21.296Z'
---

Not every team is ready to move production infrastructure overnight. Migrating a large or regulated production database (especially one deeply integrated with legacy systems or vendor-specific tooling) can be complex and time-consuming. But that doesn’t mean you need to wait to take advantage of Neon’s speed, flexibility, and branching workflows.
Some teams choose to adopt Neon first for development, testing, CI/CD, or preview environments, while keeping production on platforms like AWS RDS. This approach allows developers to instantly spin up isolated Postgres environments, test against production-like data, and iterate faster, without the overhead or risk of a full migration.
Neon’s Neon Twin workflow makes this easy to adopt without changing your production pipeline.

![Branching diagram 4](/images/pages/flow/branching-diagram-4.png)

1. **Create a Neon project for dev/test**. Use the `main` branch as the baseline for development and test environments.
2. **Import production data into `main`**. Keep your Neon environment in sync with production using `pg_dump` / `pg_restore` or logical replication.
3. **Derive child branches from `main` as needed**. Examples (see [Common branching workflows](/flow#workflows)):
   - `dev-alice`, `dev-bob` (per developer)
   - `preview-pr-42` (per PR)
   - `qa-metrics-test` (for load or feature testing)
4. **[Integrate with GitHub Actions](/docs/guides/neon-twin-partial-pg-dump-restore)** or similar CI pipelines to automatically:
   - Create branches at the start of a workflow
   - Run tests or deploy previews
   - Clean up by deleting branches after work is complete


# Production lives on Neon

---
title: 'Production lives on Neon'
subtitle: 'Run production and non-production environments on Neon with secure, isolated branching workflows for every use case'
updatedOn: '2025-07-08T12:47:21.296Z'
---

You use Neon to run both production and non-production environments. This is the most common setup for teams that want a fully serverless Postgres workflow leveraging branching to isolate dev, test, and staging environments without duplicating infrastructure.

## Single project

Your application has one primary database that serves all users. You manage all your environments (e.g. production, dev, staging, previews) within a single Neon project using branches to isolate workflows.

### No PII in production

Not all production databases include personally identifiable information. If this is your case, you can safely use production-like data in non-production environments. Follow this pattern:

![Branching diagram 1](/images/pages/flow/branching-diagram-1.png)

1. **Use `main` as your production branch**. This holds your live application data and schema.
2. **Create a long-lived dev branch**, calling it something like `main-dev`. You’ll use this as the base for all development and testing environments.
3. **Derive non-prod environments from `main-dev`**. Examples (see [Common branching workflows](/flow#workflows)):
   - `dev-alice`, `dev-bob` (per developer)
   - `preview-pr-42` (per PR)
   - `qa-metrics-test` (for testing feature flags, upgrades, etc.)
4. **Reset environments regularly**. Use branch resets to keep them aligned with `main-dev`, or delete and recreate branches as needed.

### PII in production

If your production database includes sensitive data such as user names and emails, payment or health information, or internal records, then non-prod environments must avoid exposing this data. Here’s a recommended branching architecture for this scenario.

![Branching diagram 2](/images/pages/flow/branching-diagram-2.png)

1. **Use `main` as your production branch**. This is your live environment, containing real user data.
2. **Create a schema-only branch from `main`**. This duplicates only the database structure (tables, views, functions) without copying any sensitive data.
3. **Load anonymized data into the schema-only branch**. Use Neon’s integration with PostgreSQL Anonymizer, or your own masking scripts, to populate the branch with safe test data that mirrors production shape and scale.
4. **Promote this branch as your template for non-prod environments**. Name it something like `main-anon` or `dev-anon`. This becomes the base for all development, preview, and QA branches.
5. **Derive all non-prod environments from `main-anon`**. Examples (see [Common branching workflows](/flow#workflows)):
   - `dev-alice`, `dev-bob` (per developer)
   - `preview-pr-42` (per PR)
   - `qa-metrics-test` (for load or feature testing)
6. **Reset environments regularly**. Use branch resets to keep them aligned with `main-anon`, or delete and recreate branches as needed.

> Once this workflow is set up, you only need to maintain `main-anon`. All other branches, whether created by a developer or a CI job, can be reset, recycled, or deleted without risk. This makes it easy to support many environments without multiplying infrastructure or accidentally leaking sensitive data.

## Project per customer

If your architecture provisions a dedicated Neon project for each customer, you’ll need to manage development and testing environments on a per-project basis.

This setup is common for multi-tenant SaaS platforms that offer database-level isolation per customer - for example, platforms handling sensitive or regulated data, or those offering enterprise-grade SLAs with strict data separation.

Here’s how to structure branching in this model:

![Branching diagram 3](/images/pages/flow/branching-diagram-3.png)

1. **Create a dedicated Neon project for development and testing**. This non-prod project serves as the shared workspace for all ephemeral environments.
2. **Load testing data into the `main` branch**. This branch holds a sanitized dataset that reflects the structure and scale of production. It acts as the base for all dev/test environments.
3. **Derive child branches from `main` as needed**. Examples (see [Common branching workflows](/flow#workflows)):
   - `dev-alice`, `dev-bob` (per developer)
   - `preview-pr-42` (per PR)
   - `qa-metrics-test` (for load or feature testing)
4. **Reset environments regularly**. Use branch resets to keep them aligned with `main-anon`, or delete and recreate branches as needed.


# Projects

---
title: 'Projects'
subtitle: 'Learn how Neon projects organize branches, compute endpoints, and access controls for scalable database management'
updatedOn: '2025-07-08T12:47:21.296Z'
---

In Neon, a project is the top-level unit for managing your database. If you're used to traditional Postgres deployments, think of it as everything you’d normally configure around an instance, packaged up and ready to branch.

A project includes:

- A default branch (typically `main`)
- Any number of additional branches
- One or more compute endpoints (used to run queries)
- Role-based access controls
- Storage, usage, and billing settings

All branches in a project share the same storage backend, which is what makes Neon’s branching fast, efficient, and scalable.


# Resources and next steps

---
title: 'Resources and next steps'
subtitle: 'Explore documentation, guides, and integrations to get the most out of Neon branching workflows'
updatedOn: '2025-07-08T12:47:21.296Z'
---

Neon branches set a powerful new standard to manage Postgres environments.
This guide introduced you to the core concepts, architecture patterns, and real-world workflows behind branching in Neon. From per-developer sandboxes to agent-managed snapshots and PR previews, branches give you infrastructure that keeps pace with your team and disappears when you’re done.

The best part? It’s easy to get started.

[Sign up for Neon](https://console.neon.tech/signup) (it’s free) and create your first project. In just a few minutes, you can spin up your first branch, run a test, preview an app, or connect to Vercel or GitHub Actions.

If you have any questions, [reach out to us on Discord](https://discord.gg/92vNTzKDGp).

**Branching resources**

## Documentation

- Neon Object Hierarchy
- [Branching in Neon](/docs/guides/branching-intro)
- [Schema-only branches](/docs/guides/branching-schema-only)
- [PostgreSQL Anonymizer](/docs/workflows/data-anonymization)
- [Reset from parent](/docs/guides/reset-from-parent)
- [Instant restores](/docs/introduction/branch-restore)
- [Neon CLI Reference](/docs/cli)
- [Neon API](/docs/api)

## Integrations

- [The Neon Github Integration](/docs/guides/neon-github-integration)
- [Vercel + Neon Integration](/docs/guides/vercel-overview)
- [Terraform Provider for Neon](/docs/reference/terraform)

## Guides and tutorials

- [Automate branching with GitHub Actions](/docs/guides/branching-github-actions)
- [A branch for every Vercel environment](/docs/get-started-with-neon/workflow-primer#a-branch-for-every-environment)
- [Preview branches with Fly.io](https://github.com/neondatabase-labs/preview-branches-with-fly)
- [Logical Replication](/docs/guides/logical-replication-guide)
- [Create a Neon Twin](/docs/guides/neon-twin-intro)

## Support and Community

- [Neon Discord](https://discord.gg/92vNTzKDGp)
- [Contact Support](/contact-sales)


# Rethinking the database

---
title: 'Rethinking the database'
subtitle: "Discover how Neon's branching model transforms database workflows with instant, ephemeral environments"
updatedOn: '2025-07-08T12:47:21.296Z'
---

Neon replaces these outdated workflows with a more powerful model: ephemeral, on-demand environments backed by database branching.

Instead of creating and managing separate database instances for every task, teams work from a single source of truth (a production-like parent branch) and create lightweight, fully functional clones for development, testing, and preview workflows.

The result: faster development cycles, safer experimentation, and simpler infrastructure management.

<TestimonialsWrapper>

<Testimonial
text="We’re a small team, but we’re scaling quickly and doing a lot. We’re shipping multiple times a day — to do that, we need to test stuff quickly and merge to main very quickly as well. Neon branches are a game changer for this."
author={{
  name: 'Avi Romanoff',
  company: 'Founder at Magic Circle',
}}
simpleMode
/>

<Testimonial
text="Neon’s branching paradigm has been great for us. It lets us create isolated environments without having to move huge amounts of data around. This has lightened the load on our ops team, now it’s effortless to spin up entire environments."
author={{
  name: 'Jonathan Reyes',
  company: 'Principal Engineer at Dispatch',
}}
simpleMode
/>

<Testimonial
text="Developers already face significant delays when working on a PR — running CI tests, ensuring everything is ready for preview, it all adds up. Time to launch is crucial for us: when we tried Neon and saw that spinning up a new branch takes seconds, we were blown away."
author={{
  name: 'Alex Co',
  company: 'Head of Platform Engineering at Mindvalley',
}}
simpleMode
/>

</TestimonialsWrapper>


# Tooling and automation

---
title: 'Tooling and automation'
subtitle: 'Automate branch management with Neon API, CLI, and CI/CD integrations for efficient workflows'
updatedOn: '2025-07-08T12:47:21.296Z'
---

## Neon API

Neon offers the most feature-complete [API](https://api-docs.neon.tech/reference/getting-started-with-neon-api) on the market for developers and agents that need to create, manage, and scale thousands of branches programmatically. An example of what you can do via the Neon API:

- Create a branch per PR, test run, or user/agent session
- Reset or delete branches
- Tracking compute time, data written, and storage usage at the branch level.
- Connect compute endpoints on demand
- Combine it with Neon’s hosted MCP server to manage branches in real time

```
POST /projects/{project_id}/branches
{
  "branch": {
    "name": "preview-pr-142",
    "parent_id": "main"
  }
}
```

## Neon CLI

The [Neon CLI](/docs/reference/neon-cli) lets you create, reset, and delete branches from the terminal or in scripts. deal for integrating into Git hooks, dev onboarding scripts, or CI setup steps.

```
# Create a new branch from main
neon branch create preview-pr-101 --parent main

# Reset a branch to match its parent
neon branch reset dev-bob

# Delete a branch
neon branch delete preview-pr-101
```

## CI/CD

- [GitHub integration](/docs/guides/neon-github-integration). Automatically creates, resets, and deletes Neon branches in response to pull request actions using ready‑made GitHub Actions workflows.
- [Vercel integration](/docs/guides/vercel-managed-integration). Every Vercel preview deploy triggers a matching Neon branch, with DATABASE_URL injected automatically and seamless cleanup when previews end.
- Terraform [Community]. Manage branches with IaC.


