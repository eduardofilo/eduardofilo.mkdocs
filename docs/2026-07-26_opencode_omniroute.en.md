title: OpenCode, OmniRoute, and Ponytail Installation
summary: Installing and configuring OpenCode with OmniRoute and Ponytail for AI agent programming while minimizing quotas use and costs.
date: 2026-07-26 12:00:00

![OpenCode + OmniRoute](images/posts/2026-07-26_opencode_omniroute/opencode_omniroute.png)

AI-assisted development began as intelligent line-level code completion. It evolved into a "second opinion" that reviewed file-level code and suggested changes. In the last two years, a major step forward has been taken to reach the current paradigm, *agentic development*: an agent that works at the project-level, edits files, executes commands, performs changes that were previously only suggested, runs tests, and iterates until the task is complete. The problem is that all commercial tools of this type (Claude Code, Cursor, Devin, Copilot, Codex, etc.) share two limitations: a monthly subscription and quotas that run out just when the session is getting interesting. Because here we don't consider the use via API, which for the personal scope is unaffordable.

There is also a third, quieter but also expensive problem: agents tend to **over-build**. They are asked for a date picker and end up installing a library, writing a wrapper component, and adding a stylesheet. Every extra line is paid for twice: in tokens when generating it and in tokens every time it re-enters the context.

This article describes how to set up a complete agentic development environment by combining three open-source projects that address these exact limitations:

* [**OpenCode**](https://opencode.ai/): the terminal-based programming agent.
* [**OmniRoute**](https://omniroute.online/): the model router/gateway that powers the agent.
* [**Ponytail**](https://github.com/DietrichGebert/ponytail): the *skill* that enforces minimal code discipline on the agent.

## Product Description

### OpenCode

OpenCode is an open-source programming agent that runs in the terminal (TUI) and, most importantly for our purpose, is **model-provider agnostic**. Unlike Claude Code (tied to Anthropic) or Codex (tied to OpenAI), OpenCode allows configuring any provider, including those exposing an OpenAI-compatible API, which today is practically all of them.

Its main features:

* Terminal interface with persistent sessions, context management, and *undo* for applied changes.
* Access to tools: file reading and writing, command execution, repository search, version control.
* Per-project context file (`AGENTS.md`) generated with `/init` to instruct the agent on repository conventions.
* MCP (*Model Context Protocol*) support to add external tools.
* Non-interactive CLI mode (`opencode run "..."`) for automations and scripts.
* Specialized agents and work modes (e.g., a *plan* mode that makes no changes, designed for the pre-planning phase).

### OmniRoute

OmniRoute is a local, open-source AI *gateway*. It is installed on your own machine (or a VPS), sets up an OpenAI-compatible API endpoint and a web administration panel, and from there routes each request to any of the hundreds of cataloged providers, about 90 of which have a free tier.

The interesting thing is not the catalog itself, but what it does with it:

* **Automatic routing**: using the `auto` virtual model, OmniRoute builds a *combo* of your connected providers and chooses one for each request based on live scoring. Variants exist: `auto/coding` (quality for code generation), `auto/fast` (lowest latency), `auto/cheap` (cheapest per token), and `auto/offline` (most available quota margin).
* **Cascading fallback**: when a provider returns a quota error, rate limit, or 4xx-5xx, the request is transparently retried against the next provider in the list. This prevents the classic "quota exceeded, come back in five hours" message.
* **Context compression**: a set of engines that trim the prompt (deduplication, history pruning, file compacting), enabling significant token savings, especially valuable when working with free tiers measured in tokens/day.
* **Control panel** at `http://localhost:20128` with per-provider usage stats, API key management, and assisted configuration for common CLI tools.
* **Local-first**: provider keys and traffic stay on your machine; OmniRoute is not a cloud service requiring a subscription.

### Ponytail

Ponytail is a ***skill***, a set of instructions injected into the agent's context every turn to modify its behavior. Its sole mission is to combat over-engineering by forcing the agent to go through a decision ladder before writing a single line, stopping at the first rung that solves the problem:

```txt
1. Does this need to exist?   → no: don't do it (YAGNI)
2. Already in this codebase?  → reuse it, don't rewrite
3. Stdlib does it?            → use it
4. Native platform feature?   → use it
5. Installed dependency?      → use it
6. One line?                  → one line
7. Only then: the minimum that works
```

The project's canonical example, which we referenced in the introduction, sums it up well: when asked for a date picker, the result is no longer a library plus a component but, thanks to Ponytail, `<input type="date">`.

Two important nuances:

* The ladder is applied **after** understanding the problem, not instead of it. The agent is still required to read the affected code and trace the actual flow before picking a rung. Lazy about the solution, never about reading.
* Four things are never cut: trust-boundary validation, data-loss handling, security, and accessibility. The rule is not "fewer tokens," it's "only what the task needs."

According to the project's published *benchmark* (real agent sessions on a FastAPI + React repo, with and without the *skill*), results vs. the baseline show 54% fewer lines of code, 22% fewer tokens, 20% lower cost, and 27% less time, with no penalty to security checks. As always with *benchmarks*, take them as an order of magnitude rather than a promise: savings are huge where there's a clear over-build trap and near zero where code was already minimal.

Ponytail works with a good number of agents (Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor, Devin...), and OpenCode is one of those with first-class *plugin* support.

### The Value of the Combination

Separately each piece is useful, but combined, the limitations mentioned at the beginning vanish. Each covers a different layer and they don't overlap: OmniRoute decides **who** responds, OpenCode decides **what** is done, and Ponytail decides **how much** code is written.

| Problem | How the combination solves it |
| --- | --- |
| Monthly subscription | OpenCode is free and OmniRoute connects to dozens of providers' free tiers. The entry cost is €0. |
| Quota exhaustion | OmniRoute's fallback jumps to the next provider without interrupting the agent's session. |
| Provider dependence | The agent only knows one endpoint (`localhost:20128/v1`); changing models or providers requires no changes to the agent. |
| Excessive token consumption | OmniRoute's compression engines reduce the size of agent prompts, which are typically large due to repository context. |
| Lack of spending visibility | The OmniRoute panel centralizes consumption across all providers and connected tools. |
| Oversized code | Ponytail trims what the agent builds, reducing code to review, maintain, and re-enter context in future sessions. |

The combination of these three pieces has a multiplier effect on available quota: Ponytail reduces output tokens (less code generated), OmniRoute compression reduces input tokens (less context sent), and fallback utilizes every connected provider's quota.

An additional benefit: since OmniRoute exposes a standard endpoint, the same gateway simultaneously serves OpenCode in the terminal, a VSCode extension, or any other OpenAI-compatible client. Configure once, use everywhere.

!!! Tip "Modest models, better results"
    An interesting side effect of Ponytail is that it makes working with free (typically smaller) models more viable. The less code a model is asked to generate, the fewer chances it has to make a mistake; the *skill* specifically reduces the size of the task in each step.

!!! Warning "About Free Tiers"
    Provider free tier conditions change frequently and some disappear without notice. The advantage of the OmniRoute approach is that these changes are absorbed by the gateway (by connecting another provider) without touching the agent's configuration. It's also wise to review each free provider's privacy policy before sending them code from a sensitive project.

## Installation

The entire procedure was performed on Linux. On Windows and MacOS, the steps are equivalent, only the method of installing requirements changes.

All three projects are distributed via npm, so the only common requirement is a recent version of Node.js (v22 or higher).

```bash
node --version
```

### OpenCode Installation

The recommended way is through the official install script:

```bash
curl -fsSL https://opencode.ai/install | bash
```

Alternatively, depending on the system:

```bash
npm install -g opencode-ai                  # npm (also bun, pnpm, or yarn)
brew install anomalyco/tap/opencode         # MacOS / Linux with Homebrew
sudo pacman -S opencode                     # Arch Linux (official repos)
paru -S opencode-bin                        # Arch Linux (AUR, latest version)
```

Verify the installation by launching the agent in any directory:

```bash
opencode
```

At this point, OpenCode will start but ask for provider credentials. No need to provide any yet: OmniRoute will fill that gap. For now, simply exit the program.

### OmniRoute Installation

```bash
npm install -g omniroute
omniroute
```

The `omniroute` command starts both the API and the web panel on port `20128`:

* Panel: `http://localhost:20128`
* OpenAI-compatible API: `http://localhost:20128/v1`

Other deployment methods exist, useful if you want to keep the gateway running permanently:

```bash
docker run omniroute                        # container
```

Besides the npm package and container, the project distributes a desktop app (Electron), arm64 images (works on a Raspberry Pi), and is executable on Android via Termux. An interesting option is to leave OmniRoute running on a VPS or home server and point all development machines at it.

### Ponytail Installation

Ponytail isn't installed on the system; it's declared as an OpenCode *plugin*. Simply add this entry to your `opencode.json` configuration file (the next section shows the full file with this and the other pieces):

```json
{ "plugin": ["@dietrichgebert/ponytail"] }
```

OpenCode downloads the package from npm the first time it starts with this configuration. If you prefer working with a local repo copy to modify rules, clone it and point to the *plugin* file:

```bash
git clone https://github.com/DietrichGebert/ponytail.git ~/ponytail
```

```json
{ "plugin": ["/home/user/ponytail/.opencode/plugins/ponytail.mjs"] }
```

Relative paths (like `./.opencode/plugins/ponytail.mjs`) resolve relative to the `opencode.json` declaring them; to share a single *checkout* across projects, use the absolute path, as shown in the example.

!!! Tip "Works Without a Plugin Too"
    The repo includes rules in `AGENTS.md` format and rule formats for Cursor, Devin, Cline, Kiro, Copilot, etc. Copying that file to your project yields the same always-on behavior in almost any agent. The OpenCode *plugin* specifically adds the `/ponytail` commands and intensity levels.

## Joint Configuration

The integration involves OpenCode stopping direct talk to providers to speak only to OmniRoute, while Ponytail is injected at every turn of the conversation. There are five steps.

### 1. Connect Providers in OmniRoute

With `omniroute` running, open `http://localhost:20128` and go to the **Providers** section (I recommend setting the interface to `English`, otherwise you'll see many strings prefixed with `__MISSING__`; also use the search field, as the number of configuration groups in OmniRoute is huge). The catalog appears there with an indicator for free tiers. Connect **several**, as the system's value lies in redundancy: when one runs out of quota, the others remain available. Providers requiring no key (`No Auth`) are connected by default.

The catalog is classified by **categories**, and the category determines the connection procedure:

| Category | How to connect |
| --- | --- |
| *No Auth* | They are active from the start. Although we will deactivate some as we see later. |
| *Free Tier* | Free tier that requires signing up with the provider and pasting an API key. |
| *OAuth* | Sign-in button for providers where you already have an account: OmniRoute opens the provider flow and saves the resulting *token*. |
| *API Key* | Paid providers (some with initial free credits); paste the key. |
| *Local* | Models running on your own machine (Ollama, LM Studio, vLLM…); specify the local URL. |

The top filter allows you to narrow down to your interests, and the search bar accepts the provider's name or ID.

#### No Auth Providers

In general, the selection and configuration of providers is the most complicated, cumbersome, and time-consuming part of the entire process described in this article.

Not only that, but some of the providers activated by default, such as those in the "No Auth" category, can cause problems. During the first sessions of using OpenCode, I observed that most requests returned empty responses. After investigating, I found that the issue was caused by the intervention of the "Augment (Auggie CLI)" provider, which I therefore recommend deactivating.

Additionally, checking the logs in the OmniRoute console (`Monitoring > Logs`), I found that the providers "Chipotle Pepper AI (Free)" and "DuckDuckGo AI Chat" always failed, so although they don't introduce incorrect responses like "Augment (Auggie CLI)", they delay the provider cascade traversal, so I recommend deactivating them as well. We will deactivate the "Veo AI Free" provider, as it only offers video models that we won't use for coding.

#### Free API Key Providers

The procedure is always the same, only the site for obtaining the key changes:

1. Sign up with the provider and generate an API key in their panel (the link is usually in the provider's own card in OmniRoute).
2. In OmniRoute, go to **Providers** → search for the provider → click connect/configure.
3. Paste the key into the form and save.
4. Click the **Test** button on the provider card. If it responds correctly, its models join the gateway catalog and automatically enter the `auto` model pool.

The providers in this category are those that will allow us to take full advantage of OmniRoute. They are numerous, but as mentioned in the previous section, it requires quite a bit of work to configure them (obtaining API keys from different providers) and to stay up to date with which ones change in operation or are more or less recommended at a given time.

Some documents to follow to keep the list of free providers in good shape are the following:

* [Providers Guide - Best Free Providers](https://github.com/diegosouzapw/OmniRoute/wiki/Providers-Guide#best-free-providers)
* [FREE TIERS GUIDE](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.49/docs/getting-started/FREE-TIERS-GUIDE.md)
* [FREE TIERS](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.49/docs/reference/FREE_TIERS.md)

Some of the providers in this type that I find recommendable at the time of writing this article are:

* [Gemini (Google AI Studio)](https://aistudio.google.com/api-keys)
* [Groq](https://groq.com/)
* [Mistral](https://console.mistral.ai/)
* [Cloudflare Workers AI](https://dash.cloudflare.com/): After entering the API Key, the attempt to connect to the models will fail, indicating that an "Account ID" is also required. The "Account ID" is the hash that appears below the URL `https://dash.cloudflare.com` once the session is created and started. We will enter that hash in the "Account ID" field of the provider settings.
* [Pollinations AI](https://enter.pollinations.ai/): Although the connection box indicates that the API Key is optional, it is better to create one.

#### OAuth Providers

With these, there's no key to copy: click the connection button, sign in through the provider's browser flow, and OmniRoute will save encrypted credentials in its local database. This applies to existing tool accounts (Copilot, Cursor, Kilo Code, Qoder, etc.).

!!! Warning "Review Terms of Service"
    Several of these providers are services designed for their own clients; some expressly prohibit use via proxies or third-party clients. The OmniRoute provider card includes a warning when this is the case. It's wise to read these notices before connecting an account you want to keep.

#### Curating the Pool for Agentic Use

There is one issue that isn't mentioned in the OmniRoute documentation and that, in my experience, has been essential to getting the setup up and running. The point is that **not all vendors in the catalog are suitable for assigning to an agent**.

The reason is that an agent like OpenCode doesn't just ask for text: every request carries the list of *tools* at its disposal (read files, run commands, search the repository…) and it expects the model to reply with calls to those tools. Providers that are the official API of a model return those calls to the client, which is the correct behaviour. But the catalog also includes two kinds of entries that behave differently:

* **Proxies of a web client** (those you connect to with a chat session cookie rather than an API key). The service on the other end has its own tool engine and tries to execute the tools itself, in its own environment, instead of returning them.
* **Agent front-ends** (services designed to be consumed from their own command line tool). They ship their own tool catalog and don't fit as the engine behind another agent.

The symptom is baffling, because the agent reports no error at all: it simply returns an empty response, or a text in which the model explains that it could not explore the repository and asks us, for example, to paste the contents of the files ourselves.

##### An Admission Test

The reliable way to decide whether a provider belongs in the pool is to ask the gateway: send a request with a tool and check whether the model invokes it. The response must contain a `tool_calls` block with the tool name and its arguments; if prose arrives instead, that provider is no good.

A single request against `auto/coding` is not enough to validate the pool. `auto` routing tends to stick to the last working provider and does not guarantee that all candidates receive traffic. Each provider must be tested separately.

The problematic behavior we want to detect (proxies that execute tools themselves, front-ends with their own tool catalog) is a property **of the provider**, not of the individual model: a proxy either passes `tool_calls` back to the client or it doesn't, regardless of which model sits behind it. That is why it is enough to test **one representative model per provider**, identified by the prefix before the slash (`groq/`, `mistral/`, `cf/`...), instead of the hundreds of models in the catalog. In reality we will test the first 5 models of each provider in case one fails for some specific reason. The `jq` filter excludes only the virtual `auto/*` models:

```bash
API="http://localhost:20128/v1"
KEY="sk-your-omniroute-key"

# List of providers (excluding auto/*)
providers=$(curl -s "$API/models" -H "Authorization: Bearer $KEY" \
  | jq -r '[.data[].id | select(startswith("auto/") | not)]
           | group_by(split("/")[0]) | map(.[0]) | .[]' \
  | cut -d/ -f1 | sort -u)

for prov in $providers; do
  # Up to 5 models from this provider
  prov_models=$(curl -s "$API/models" -H "Authorization: Bearer $KEY" \
    | jq -r --arg p "$prov" '[.data[].id | select(startswith($p+"/"))][:5][]')
  status=""
  tested=""
  for model in $prov_models; do
    tested="$model"
    resp=$(curl -s -i "$API/chat/completions" \
      -H "Authorization: Bearer $KEY" \
      -H "Content-Type: application/json" \
      -d "{\"model\":\"$model\",\"stream\":false,\"messages\":[{\"role\":\"user\",\"content\":\"Read the file /etc/hostname\"}],\"tools\":[{\"type\":\"function\",\"function\":{\"name\":\"read\",\"description\":\"Reads a file\",\"parameters\":{\"type\":\"object\",\"properties\":{\"path\":{\"type\":\"string\"}},\"required\":[\"path\"]}}}]}")
    http_code=$(printf '%s' "$resp" | head -1 | grep -o '[0-9][0-9][0-9]')
    body=$(printf '%s' "$resp" | sed -n '/^\r\?$/,$p' | tail -n +2)
    if [ "$http_code" = "200" ]; then
      if printf '%s' "$body" | jq -e '.choices[0].message.tool_calls[0].function.name' >/dev/null 2>&1; then
        status="OK"
      else
        status="FAIL (no tool_calls)"
      fi
      break
    elif [ "$http_code" = "401" ] || [ "$http_code" = "403" ]; then
      status="FAIL (auth $http_code)"
      break
    else
      continue  # 404, 400... model unavailable, try the next one
    fi
  done
  [ -z "$status" ] && status="FAIL (no valid models)"
  printf '%-24s %-45s %s\n' "$status" "$prov" "$tested"
done
```

Requires `jq`. The script distinguishes three failure causes:

* **`FAIL (no tool_calls)`**: the provider returned a 200 but with prose instead of a tool call. This is the problem we are after: a proxy that runs the tools itself or a front-end with its own catalog. => Disconnect it.
* **`FAIL (auth 401/403)`**: the provider's key is expired, misconfigured, or out of quota. This is not a *tools* problem but a configuration one. => Fix the connection in **Providers** (or disconnect it if there's no remedy).
* **`FAIL (no valid models)`**: every model tested returned 404 or 400. The provider is down or its catalog has changed. => Review it in **Providers**.

In the output, the right-hand column shows the model that produced the result. This is a one-time setup step that you only need to repeat when adding a new provider.

##### Two Symptoms to Spot in the Logs

In `Monitoring > Logs` there are two patterns that give away a provider worth retiring:

* **`200` with `TO: 0`** in a few milliseconds: the provider returned an empty response with a success status. A real inference never takes 15 ms.
* **Slow responses whose content is text** where `tool_calls` should be, often carrying error messages from the remote service itself explaining that the tools don't exist.

!!! Warning "Fallback doesn't trigger on failures disguised as success"
    It's worth understanding the limits of the system. OmniRoute's retry cascade works with **explicit** failures: a 429 for quota, a 502 or a timeout cause the request to be retried against the next provider, and this is perfectly visible in the log. But the two cases above reach the gateway as correct responses: a `200` with an empty body is, to a router, a valid response. No gateway can arbitrate that without semantically inspecting the content of every response.

    Hence curating the pool is our responsibility, and it's a step that shouldn't be skipped. Put another way: **automatic routing is only as good as the worst apparently healthy provider in the pool**.

### 2. Create an OmniRoute API Key

In the panel, go to **API Manager** → **Create API Key**. Give it a descriptive name (e.g., `opencode`) and copy the generated key, which looks like `sk-xxxxxxxx-xxxxxxxx`.

This is a local key: it's used by your clients (OpenCode in this case) to authenticate against OmniRoute and has nothing to do with provider keys, which are held by OmniRoute.

You can verify the gateway is responding and see available models:

```bash
curl http://localhost:20128/v1/models -H "Authorization: Bearer sk-your-omniroute-key"
```

### 3. Declare OmniRoute as a Provider in OpenCode

OpenCode supports any OpenAI-compatible provider by declaring it in its config file. To apply configuration globally, write it to `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["@dietrichgebert/ponytail"],
  "provider": {
    "omniroute": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "OmniRoute",
      "options": {
        "baseURL": "http://localhost:20128/v1",
        "apiKey": "sk-your-omniroute-key"
      },
      "models": {
        "auto": { "name": "Auto (balanced)" },
        "auto/coding": { "name": "Auto (coding quality)" },
        "auto/cheap": { "name": "Auto (cheapest)" },
        "auto/fast": { "name": "Auto (fastest)" },
        "auto/offline": { "name": "Auto (max quota)" }
      }
    }
  },
  "model": "omniroute/auto/coding"
}
```

Important points of this configuration:

* `npm`: the `@ai-sdk/openai-compatible` adapter is used for `/v1/chat/completions` endpoints, which OmniRoute uses.
* `options.baseURL`: the gateway endpoint. If OmniRoute is on another machine, use its IP or domain here.
* `options.apiKey`: the API key created in OmniRoute.
* `models`: no need to list specific provider models; simply declare the `auto` virtual models to enable smart routing and fallback. To fix a specific model, add it using the ID returned by `/v1/models` (see [previous point](#2-create-an-omniroute-api-key)).
* `model`: default model at startup. `auto/coding` is a good choice for development; `auto/offline` is useful when quota headroom is the priority.
* `plugin`: the list of OpenCode *plugins*, where Ponytail belongs.

!!! Tip "Key Outside the Config File"
    If the config file will be versioned (e.g., in a *dotfiles* repo), it's better not to write the key in it. OpenCode allows storing credentials with `/connect` (choose *Other*, ID `omniroute`), in which case you can omit `options.apiKey` from the JSON.

You can also place an `opencode.json` file in a specific project's root, merging its settings with the global ones. This is practical for forcing a different model for a specific project.

### 4. Adjust Ponytail Level

Ponytail needs no config file: it works as soon as it's declared as a *plugin*. The only thing to decide is the **intensity level**, which can be changed on the fly from the TUI:

```txt
/ponytail            → reports current level
/ponytail lite       → mild trimming
/ponytail full       → default level
/ponytail ultra      → aggressive trimming
/ponytail off        → disabled for this session
```

The default level is `full`. To set a different default for all new sessions, use the `PONYTAIL_DEFAULT_MODE` environment variable or the `defaultMode` field in `~/.config/ponytail/config.json`:

```bash
export PONYTAIL_DEFAULT_MODE="full"
```

While active, the ruleset is also injected into subagents spawned by the main agent. To exclude some (e.g., read-only search agents), use a regex against the subagent type defined in the following environment variable:

```bash
export PONYTAIL_SUBAGENT_MATCHER="build|code"
```

### 5. Verify Integration

Start the agent and verify the provider appears:

```bash
opencode
```

Within the TUI, the `/models` command should show OmniRoute entries.

From a directory containing a repository or project, run a quick test in CLI non-interactive mode:

```bash
opencode run "Summarize this repo in three lines" --model omniroute/auto/coding
```

While it runs, the OmniRoute panel (`Monitoring > Logs`) shows in real-time which provider handled the request, tokens consumed, and compression savings. If a provider fails, the log shows the automatic jump to the next.

To check if Ponytail is loaded, simply run `/ponytail` in the TUI (it returns the active level) or `/ponytail-help` (lists its commands).

!!! Warning "Apparent Ponytail Startup ERROR"
    If OpenCode is started with `--print-logs`, this line may appear when loading the configuration:

    ```txt
    ERROR message="failed to load plugin" path=@dietrichgebert/ponytail error="path must be a string or a file descriptor"
    ```

    It's misleading: OpenCode tries to load the plugin by two paths and one of them fails, but the other loads it correctly. The test that Ponytail is operational is that `/ponytail` responds with the active level. Note that the level is **persisted** between sessions (in `~/.config/opencode/.ponytail-active`): a `/ponytail off` from a previous test leaves the plugin loaded but disabled. When in doubt: `/ponytail full` and ask the agent what its *system prompt* says about `PONYTAIL`.

!!! Tip "Environment Variables for Other Tools"
    Exporting these variables in your `.bashrc` or `.zshrc` makes any other OpenAI-convention-respecting tool use the gateway without further configuration:

    ```bash
    export OPENAI_BASE_URL="http://localhost:20128/v1"
    export OPENAI_API_KEY="sk-your-omniroute-key"
    ```

## Project Types and Operations

Once the environment is set up, the workflow is essentially the same regardless of language, project size, or task nature. What changes between cases is not the procedure, but the choice of model, trimming level, and context preparation. Thus, we first describe the common flow and then the adjustments per project type.

### Common Operations

1. **Navigate to the repository and start the agent**:

    ```bash
    cd my-project
    opencode
    ```

2. **Generate the context file** the first time using the `/init` command in the TUI. OpenCode explores the repo and writes an `AGENTS.md` with the project description, build/test commands, and detected conventions. It's worth reviewing and manual completion; it's the most influential document for result quality and should be versioned with the project.

3. **Plan before executing**. For any non-trivial change, ask for a plan first rather than direct implementation. OpenCode has a planning mode that doesn't write to disk; reviewing a plan costs much less than reviewing a 400-line incorrect *diff*.

4. **Iterate in small steps**, validating with your project tools (compiler, *linter*, tests) after each step. The agent can execute these commands itself if documented in `AGENTS.md`.

5. **Pass the Ponytail review** before finalizing the task with `/ponytail-review`. It analyzes the current *diff* for over-engineering and returns a delete-list. This step quickly pays off in saved time.

6. **Review the `diff` and commit** using version control. Always work on a branch and make small *commits*: it's the natural safety net when an agent writes the code.

7. **Clear context between tasks** with `/new`. Dragging context from a finished task worsens results and spikes token consumption. The next section details session management.

8. **Monitor the OmniRoute panel** occasionally to see which providers are in use, which are exhausted, and if compression savings are as expected.

### Session Management in OpenCode

When starting with OpenCode, it's surprising to find that sessions remain listed even after exiting the TUI with `Ctrl-d` or `/exit`. It's not a hang or incomplete closure: **a session is not a process, it's a persisted conversation**. Exiting the TUI ends the interface, but the conversation history (messages, tools, files, token usage) is stored in OpenCode's local database for later resumption. Since each `opencode` call without arguments starts a new session, you'll have dozens of entries in a few days.

In other words: "closing" doesn't mean "deleting." You must build the habit of reusing and pruning.

#### Resume Instead of Create

First, stop starting from scratch. Here are three ways to continue previous work:

```bash
opencode --continue                  # resumes the last session of the current project (-c)
opencode --session <sessionID>       # resumes a specific session (-s)
opencode --session <sessionID> --fork # forks it into a copy, leaving the original intact
```

From within the TUI, the `/sessions` command (aliases: `/resume`, `/continue`; shortcut: `Ctrl+x l`) opens a selector to switch sessions without exiting.

The `--fork` option is particularly useful when a conversation reaches an interesting point and you want to test two different paths: it forks, and each branch goes its own way, much like a `git branch`.

#### Closing Tasks Properly

Two TUI commands mark the end of a task:

* `/new` (alias: `/clear`, shortcut: `Ctrl+x n`): opens a new, clean session. Use this when switching tasks instead of continuing in the old conversation.
* `/compact` (alias: `/summarize`, shortcut: `Ctrl+x c`): summarizes the current conversation to free up the context window without losing the thread. Use this if the same task is getting too "heavy" context-wise.

To keep a session's result, `/export` dumps the conversation to Markdown and opens your editor, while `opencode export <sessionID>` does the same in JSON from the CLI.

#### Inventory and Pruning

From outside the TUI, you manage the complete inventory:

```bash
opencode session list                # list sessions
opencode session list -n 20          # limit number of entries
opencode session list --format json  # script-processable output
opencode session delete <sessionID>  # delete a session
```

To see cumulative cost, which in this setup determines how much free quota you're burning:

```bash
opencode stats                       # token usage and cost
opencode stats --days 7 --models     # last 7 days, per-model breakdown
opencode stats --project             # current project only
```

#### Workflow

Putting it all together, the routine to keep the list under control is:

1. **One session per task**, not per day or project. The natural unit is whatever ends in a *commit*.
2. **Resume with `-c`** when returning to a partial task, instead of starting `opencode` fresh and re-explaining context (which costs tokens).
3. **`/new` when switching tasks** and `/compact` if the task grows but remains the same.
4. **Export what's worth keeping** before closing a session with valuable conclusions.
5. **Periodic pruning** (e.g., weekly), reviewing `opencode session list` and deleting anything already committed that adds no value with `opencode session delete`.
6. **Review `opencode stats`** during the same prune to get the consumption picture alongside the OmniRoute panel.

!!! Tip "Sessions Are Per Project"
    OpenCode associates sessions with the working directory they were launched from; thus, `--continue` or `-c` resumes the last session *of that project*, not the last overall. This helps: always working from the repo root naturally keeps lists project-ordered.

### Ponytail Commands

Beyond intensity levels, the *skill* provides a few commands fitting different workflow stages:

| Command | Purpose |
| --- | --- |
| `/ponytail [lite \| full \| ultra \| off]` | Adjusts intensity or disables it. Reports current level if no argument is provided. |
| `/ponytail-review` | Reviews the current *diff* for over-engineering and returns a delete-list. |
| `/ponytail-audit` | Same, but for the entire repo instead of just the *diff*. |
| `/ponytail-debt` | Harvests `ponytail:` shortcuts deferred into a ledger. |
| `/ponytail-gain` | Shows the measured impact scoreboard (less code/cost, more speed). |
| `/ponytail-help` | Quick reference for the above commands. |

When the agent decides not to build something, it leaves a comment like `ponytail: browser has one`, explaining the ladder rung where it stopped. These comments are what `/ponytail-debt` harvests, so "defer for now" decisions are recorded rather than lost.

### Adjustments by Project Type

The only significant variation between scenarios is model choice and context preparation:

* **New projects from scratch (*greenfield*)**. Little context to load and lots of code to generate. Ideal for free tiers: `auto/cheap` or `auto/offline` yield good results and input token consumption is low. Start by asking for project scaffolding and dependency files, then functionalities. Ponytail shines here, as agents have more freedom to invent extra structure.

* **Maintenance and evolution of existing code**. Context is the bottleneck here; the agent needs to read significant code before touching anything. A detailed `AGENTS.md`, active OmniRoute context compression, and `auto/coding` for modifications are key. Fallback is most noticeable here due to long sessions. Ponytail's "Already in this codebase?" rung is especially valuable, preventing duplicate helpers.

* **Error debugging**. The flow is the same but works much better if you provide a way to reproduce the failure (failing test, full trace, exact command). Explicit reasoning models yield better results; choose *thinking* variants in OmniRoute. A `lite` or `off` Ponytail level might be preferable here: debugging is about understanding, not trimming.

* **Scripting and automation**. CLI non-interactive mode is useful here for integration into scripts, git hooks, or scheduled tasks:

    ```bash
    opencode run "Update CHANGELOG with commits since the last tag" \
      --model omniroute/auto/fast
    ```

* **Large, repetitive refactors**. Break work into independent tasks and launch them separately instead of one massive change. This yields better results and avoids exhausting context windows or provider quotas in one go. If slimming down legacy code is the goal, `/ponytail-audit` on the whole repo and `/ponytail ultra` are the natural starting point.

* **Sensitive code projects**. If code cannot be sent to third parties, the same setup works by connecting a local provider in OmniRoute (Ollama, LM Studio) instead of free services. Only the provider in the panel changes; OpenCode and the workflow remain the same.

## Conclusion

The combination of OpenCode, OmniRoute, and Ponytail provides a complete agentic development environment with zero entry cost and no quota interruptions. Each piece attacks a different front: the agent provides capabilities, the gateway provides quota and provider independence, and the *skill* provides discipline for minimal code generation. All three are declared in a single 20-line config file.

The price is a slightly more laborious initial setup compared to closed products and the need to occasionally check active free providers. In return, you get what subscriptions don't offer: provider independence, full consumption visibility, and less code to regret.
