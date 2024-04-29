﻿
## What's New: GemPy v3 Pre-release!

**Introducing GemPy Version 3: A Leap Froward in Geomodeling Software**

Welcome to the era of GemPy v3! We are thrilled to announce the release of the latest version, a product of meticulous planning, redesign, and rigorous testing. While the core essence remains intact, v3 brings significant enhancements and novelties that promise to revolutionize your geomodeling experience.

**1. Transition from GemPy v2 to v3: The Legacy Lives On**

The journey from GemPy v2 to v3 has been transformative. To ensure that our users don't lose out on any previous functionalities, we've shifted v2 to a package named [gempy_legacy](https://github.com/gempy-project/gempy_legacy). While the core team will not develop any new features for this version, we'll continue maintaining it based on community requests.

**2. A More Streamlined API**

GemPy v3 promises a cleaner, sleeker, and more intuitive API. With a clear end-goal in mind, we've redesigned the API and data classes to optimize utility, minimize code repetition, and boost performance.

**3. Parting Ways with Theano/Aesara**

One significant shift is our departure from Theano/Aesara. Although these technologies served us well in the past, it's time to evolve. Ensuring the long-term viability of GemPy, v3 incorporates a flexible tensor library. Currently, it supports `numpy` and has optional dependencies on `PyTorch`. Furthermore, TensorFlow's integration is in the pipeline. Impressively, with the new abstractions the PyTorch implementation took just a day!

**4. Comprehensive Refactoring for Greater Robustness**

We've overhauled the foundation of GemPy to ensure:

- **Enhanced State Management:** By employing properties, we ensure a consistently valid state, irrespective of data modifications.
- **Optimized Dependency Management:** The handling of dependencies is now more efficient and streamlined. Plus, most of them are optional.
- **Modular Design:** We've divided GemPy into multiple libraries to enhance its adaptability and ease-of-use:
    - `gempy_engine` [here](https://github.com/gempy-project/gempy_engine)
    - `gempy_viewer` [here](https://github.com/gempy-project/gempy_viewer)
    - `gempy_plugins`[here](https://github.com/gempy-project/gempy_plugins)
    - `gempy_probability` (Stay tuned for this!)
    - `gempy` (Leaner and meaner, focused mainly on documentation and the API)

**5. Octree Implementation for Faster Computation**

**6. Dual Contouring for High-Quality Meshing**

**7. First steps LiquidEarth Integration**

**And Much More!**

---

**In Conclusion**

GemPy v3 is not just an upgrade; it's a transformation that ensures longevity, adaptability, and cutting-edge functionalities. We're confident that this version will redefine geomodeling standards, and we're eager to see the fantastic work you'll accomplish with it!

Stay tuned for more updates and tutorials to help you transition smoothly to GemPy v3. Your feedback, as always, is invaluable to us. So, dive into the new version and let us know your thoughts!

