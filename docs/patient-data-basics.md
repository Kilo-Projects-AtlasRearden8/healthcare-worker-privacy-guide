# Patient Data Basics

You already know patient data deserves protection. This chapter is a plain
English refresher on what counts, why it matters, and where AI fits in.

## What counts as patient data

Patient data is any information that can identify a patient and relates to
their health, care, or payment. In healthcare you may hear this called PHI
(protected health information). Common examples:

- Names — first, last, initials, or nicknames
- Dates of birth, ages combined with other details, admission or discharge dates
- Medical record numbers (MRNs), account numbers, patient IDs
- Diagnoses, conditions, test results, medications, treatment plans
- Photos, scans, X-rays, EKGs, voice recordings, wristband numbers
- Insurance info, billing codes, claim numbers, appointment dates
- Anything that, combined with other details, could identify someone

## The "small detail" trap

You might think "I'll just paste the lab value, not the name." That is still
risky. A rare diagnosis plus a shift, unit, or age can identify a patient just
as well as a name. Even "de-identified" stories can be risky — saying "a nurse
on the night shift at County General" plus a diagnosis may be enough for
someone to figure out who you mean.

When in doubt, treat it as patient data. Keep it out of chatbots.

## Why AI chatbots are different from your EHR

Your electronic health record (EHR) is built for healthcare. It has access
logs, permissions, and audit trails so you can see who looked at what and when.

Most public AI chatbots are not built for healthcare:

- What you paste may be stored by the AI provider
- It may be used to train future models
- Humans at the provider may read it
- You usually cannot delete it fully or know exactly where it went
- Once it leaves your control, you cannot take it back

Using an AI chatbot is not the same as documenting in the EHR. Assume anything
you paste could become public.

## HIPAA in one paragraph

HIPAA (the Health Insurance Portability and Accountability Act) sets rules for
protecting patients' protected health information (PHI). Covered entities and
their business associates must follow them. Violations can mean fines,
investigation, and job loss. Your employer's policies are often stricter than
HIPAA — follow the stricter rule.

This manual is not legal advice. Ask your compliance or privacy officer about
your workplace's rules.

## Your workplace comes first

Before you use any AI tool at work:

1. Ask your privacy or compliance officer if AI use is allowed
2. Check whether your employer has an approved AI tool
3. Never paste patient data into a tool your employer has not vetted
4. Follow your employer's policy, even if this guide says something different

If your employer says no AI at work, respect that. You can still use AI safely
at home for personal learning — just keep patient data out of it.

Credit: Asdale Dynamics, LLC. Education only — never medical advice, never
legal advice. See `disclaimer.md`.
