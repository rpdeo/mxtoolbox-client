# MX ToolBox API Client

We were looking for a python language client for MXToolBox API.

We found [mxtoolbox-connect](https://github.com/madhava-aasam/mxtoolbox-connect "MX Toolbox API wrapped in JavaScript") which was written in JavaScript.

We also found [this](https://github.com/andrea-zanella/MxToolbox-API---Python "Python command line tool for MX Toolbox API") one.

Hence we wrote this taking inspiration from that code.

It is just a wrapper over httpx.get() and a bit of API command
handling. Nothing fancy. We plan to use this inside our Flask-based
IOC checking tool.

[See]( https://mxtoolbox.com/User/Api/Lookup.aspx "MX ToolBox API Docs") for API details.

You need to sign-up to get a free API key.

You get 64 free requests per day.

# Dependencies

- httpx

# Dev Dependencies

See ./requirements-dev.txt

# See also

- https://mxtoolbox.com/User/Api/Lookup.aspx
- https://github.com/madhava-aasam/mxtoolbox-connect
- https://github.com/andrea-zanella/MxToolbox-API---Python
