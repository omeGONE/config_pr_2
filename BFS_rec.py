from Searching_for_dependences import  find_package_dependencies_from_url

def BFS_rec(package, version):
    graph = []
    def BFS(package, version):
        url = f"https://api.nuget.org/v3/registration5-semver1/{package.lower()}/{version}.json"
        return find_package_dependencies_from_url(url)[".NETStandard2.0"]
    BFS(package, version)


# {"id" : "Microsoft.Bcl.AsyncInterfaces", "version" : "10.0.0"} : [{"id" : "System.Threading.Tasks.Extensions", "version" : "4.6.3"} : [{"id" : "System.Runtime.CompilerServices.Unsafe", "version" : "6.1.2"}]]