# CLAUDE.md — MyApplication2

## Project Overview

Android application that searches and displays books using the **Google Books API v1**. Users see a list of books (title, thumbnail, publication date) in a RecyclerView; tapping a card opens `BookActivity` (detail view, currently a stub).

- **Package:** `com.example.tomasferronha.myapplication2`
- **Min SDK:** 15 (Android 4.0.3) / **Target SDK:** 28 (Android P)
- **Language:** Java
- **Build system:** Gradle (Android Gradle Plugin 3.2.1)

---

## Directory Structure

```
MyApplication2/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/example/tomasferronha/myapplication2/
│   │   │   │   ├── activity/        # Activities (UI entry points)
│   │   │   │   ├── adapter/         # RecyclerView adapters
│   │   │   │   ├── model/           # POJO/data models (GSON-mapped)
│   │   │   │   ├── my_interface/    # Retrofit API interface
│   │   │   │   └── network/         # Retrofit singleton
│   │   │   ├── res/
│   │   │   │   ├── layout/          # XML layouts
│   │   │   │   └── values/          # strings, colors, styles, dimens
│   │   │   └── AndroidManifest.xml
│   │   ├── test/                    # JUnit unit tests (runs on JVM)
│   │   └── androidTest/             # Espresso instrumented tests (runs on device/emulator)
│   ├── build.gradle                 # Module-level deps & Android config
│   └── proguard-rules.pro
├── build.gradle                     # Root build script (plugin classpath)
├── settings.gradle                  # Single-module project declaration
└── gradle.properties                # JVM args (-Xmx1536m)
```

---

## Key Source Files

| File | Purpose |
|------|---------|
| `activity/MainActivity.java` | Entry point — fires Google Books API call on create, feeds adapter |
| `activity/BookActivity.java` | Detail screen — declared in manifest, body is a stub (empty layout) |
| `adapter/BookAdapter.java` | RecyclerView adapter; spawns `DownloadImageWithURLTask` per row |
| `model/Book.java` | Top-level book POJO; holds `VolumeInfo` + `selfLink` |
| `model/BookList.java` | Wraps `ArrayList<Book>` — maps to the `items` array in the API response |
| `model/VolumeInfo.java` | Title, publishedDate, nested `ImageLinks` |
| `model/ImageLinks.java` | `smallThumbnail` and `thumbnail` URL strings |
| `my_interface/GetBookDataService.java` | Retrofit interface — `GET volumes?q={query}` |
| `network/RetrofitInstance.java` | Lazy singleton Retrofit client pointed at `https://www.googleapis.com/books/v1/` |

---

## Architecture

The app follows a lightweight **MVC** pattern:

- **Model** — `model/` package: plain Java objects annotated with `@SerializedName` / `@Expose` for GSON deserialization.
- **View** — XML layouts in `res/layout/` and `ViewHolder` classes inside adapters.
- **Controller** — `Activity` classes own lifecycle and orchestrate data fetch → adapter wiring.

### Data flow

```
MainActivity.onCreate()
  └─> RetrofitInstance.getRetrofitInstance()   (singleton Retrofit)
        └─> GetBookDataService.getBookData("android")   (Retrofit call)
              └─> onResponse() → generateBookList()
                    └─> BookAdapter(ArrayList<Book>)
                          └─> onBindViewHolder()
                                └─> DownloadImageWithURLTask (AsyncTask, per row)
```

---

## Build & Run

### Prerequisites
- Android Studio (3.x or newer) or a Gradle installation with Android SDK 28
- Internet access (runtime — app fetches live API data)

### Build commands

```bash
# Debug APK
./gradlew assembleDebug

# Release APK (minification disabled — see app/build.gradle)
./gradlew assembleRelease

# Clean build
./gradlew clean assembleDebug
```

### Run on device/emulator
Use Android Studio's **Run** button, or:
```bash
./gradlew installDebug
```

---

## Testing

### Unit tests (JVM)
```bash
./gradlew test
```
Tests live in `app/src/test/`. Currently only the scaffold `ExampleUnitTest` exists.

### Instrumented tests (device/emulator required)
```bash
./gradlew connectedAndroidTest
```
Tests live in `app/src/androidTest/`. Currently only the scaffold `ExampleInstrumentedTest` exists.
Runner: `android.support.test.runner.AndroidJUnitRunner`
UI framework available: Espresso 3.0.2

---

## Dependencies

All declared in `app/build.gradle`:

| Library | Version | Use |
|---------|---------|-----|
| `com.android.support:appcompat-v7` | 28.0.0 | Base `AppCompatActivity` |
| `com.android.support:design` | 28.0.0 | `CoordinatorLayout`, `Toolbar`, FAB |
| `com.android.support:recyclerview-v7` | 28.0.0 | Book list |
| `com.android.support:cardview-v7` | 28.0.0 | Per-item card UI |
| `com.android.support.constraint:constraint-layout` | 1.1.3 | `BookActivity` layout |
| `com.squareup.retrofit2:retrofit` | 2.3.0 | HTTP client |
| `com.squareup.retrofit2:converter-gson` | 2.1.0 | JSON → POJO via GSON |
| `junit:junit` | 4.12 | Unit tests |
| `espresso-core` | 3.0.2 | Instrumented UI tests |

> **Note:** The project uses the pre-AndroidX support library namespace (`com.android.support`). Do not mix in `androidx.*` artifacts without migrating fully.

---

## Conventions & Patterns

### Package naming
- `activity/` — one file per `Activity` subclass
- `adapter/` — one file per `RecyclerView.Adapter` subclass
- `model/` — flat POJOs, no logic; GSON annotations on fields
- `my_interface/` — Retrofit service interfaces (naming is non-standard; prefer `api/` in new code)
- `network/` — networking infrastructure (Retrofit instance, interceptors, etc.)

### Singleton pattern
`RetrofitInstance` uses a null-check lazy singleton. Follow the same pattern for any new network client.

### Async work
Image downloads currently use `AsyncTask` (deprecated in API 30). New async work should use `ExecutorService` + `Handler` or a modern library like Glide/Picasso for images.

### GSON model classes
- Use `@SerializedName("fieldName")` when the JSON key differs from the Java field name.
- Use `@Expose` on fields that should be included in serialization/deserialization.
- Keep models as pure data containers — no business logic.

### Activities
- Call `setContentView(R.layout.activity_*)` in `onCreate`.
- Perform network calls in `onCreate` (no ViewModel or lifecycle-aware components present yet).
- Pass data between activities via `Intent` extras.

---

## Known Issues & Incomplete Areas

1. **`BookActivity` is a stub** — layout is an empty `ConstraintLayout`; the intent click handler in `BookAdapter` is present but the extra (`selfBook`) is commented out.
2. **`context` in `BookAdapter` is never assigned** — the `onClick` listener will throw a `NullPointerException` at runtime when a card is tapped. Either pass `Context` through the constructor or capture it in `onCreateViewHolder`.
3. **No null-safety on API response** — `response.body().getBookList()` will crash if the response body or items list is null.
4. **`AsyncTask` is deprecated** — replace with Glide or Picasso for image loading.
5. **Hardcoded search query** — `getBookData("android")` in `MainActivity`; no search UI is wired up.
6. **No data persistence** — book list is in-memory only; cleared on rotation or process death.
7. **Support libraries are not AndroidX** — migration recommended before targeting API 29+.
8. **No CI/CD pipeline** configured.

---

## Manifest Permissions

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

Both activities are registered:
- `MainActivity` — `LAUNCHER` intent filter (app entry point)
- `BookActivity` — standard activity (no intent filter)

---

## Git Workflow

- Default branch: `master`
- Feature work: use short-lived branches, merge via PR
- No pre-commit hooks or lint gates are configured
