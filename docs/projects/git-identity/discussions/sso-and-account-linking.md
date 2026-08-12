# SSO and Account Linking

**Question:** If we use the same SSO system (e.g., Keycloak) for both Django and Forgejo, is it simple to link those accounts together so a logged-in Django user is automatically associated with their Forgejo activity?

## The Problem: Brittle Linking

In a standard SSO setup, the Identity Provider (IdP) issues a unique, immutable ID (the `sub` claim) for each human. Both Django and Forgejo would know this ID.

However, when Django acts as an integration layer and queries the Forgejo API to sync PRs and issues, Forgejo typically returns its own internal username (e.g., `author: { login: "alexander" }`). It does not broadcast the underlying Keycloak `sub` ID over its public API.

Because Django cannot see the Keycloak ID in the Forgejo API response, it has to fall back to guessing: *"Is the Forgejo user 'alexander' the same as the Keycloak user 'alexander@example.com'?"* 

As soon as someone changes their email or uses a different handle on a different service, this link breaks silently.

## Alternative Approaches Evaluated

1. **Forgejo as the Identity Provider:**
   Instead of a third-party IdP, Forgejo acts as the OAuth2 provider. Django users log in via Forgejo.
   *Pros:* Linking is trivial. Django gets the exact Forgejo User ID during login.
   *Cons:* Forgejo becomes the critical identity infrastructure for the entire collective (e.g., Matrix, Nextcloud would all authenticate through Forgejo).

2. **Django as the Identity Provider:**
   Django runs an OAuth2 server, and Forgejo uses Django for login.
   *Pros:* Django has absolute control and knows the exact mapping.
   *Cons:* This heavily violates the "Django is just an integration layer" philosophy. Django becomes stateful, critical infrastructure rather than a disposable view over data.

## Conclusion

SSO is excellent for *authentication* (proving who is at the keyboard), but it is surprisingly poor at *cross-system identity linking* without deep, custom API integration between the services. 

Because we want to keep Django as a stateless integration layer, relying on SSO to link activity across systems is too brittle. This led us to explore [Federated Identity via Git](./federated-identity-via-git.md) instead.
