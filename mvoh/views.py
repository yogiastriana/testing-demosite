from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
import os, json, random


# Create your views here.
@login_required(login_url='/login/')
def permutation_dashboard_view(request):
    # Get the directory of the current file (views.py)
    current_directory = os.path.dirname(__file__)
    
    # Construct the path to the JSON file
    json_file_path = os.path.join(current_directory, 'permutation.json')

    # Load the JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Extract sectors and industries
    sectors = set()  # Using a set to avoid duplicates
    industries = set()

    for item in data:
        sectors.add(item.get("Sector"))
        industries.add(item.get("Industry"))

    # Convert sets to lists to pass to the template
    sectors = list(sectors)
    industries = list(industries)

    context = {
        "sectors": sectors,
        "industries": industries
    }

    return render(request, 'permutation-mvoh/dashboard.html', context)


@login_required(login_url='/login/')
def input_form_view(request):

    # Get the directory of the current file (views.py)
    current_directory = os.path.dirname(__file__)
    
    # Construct the path to the JSON file
    json_file_path = os.path.join(current_directory, 'permutation.json')

    # Load the JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Extract sectors and industries
    sectors = set()  # Using a set to avoid duplicates
    industries = set()

    for item in data:
        sectors.add(item.get("Sector"))
        industries.add(item.get("Industry"))

    # Convert sets to lists to pass to the template
    sectors = list(sectors)
    industries = list(industries)

    context = {
        "sectors": sectors,
        "industries": industries
    }

    return render(request, 'mvoh/index.html', context)


def get_sector_industries_view(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            selected_sectors = data.get('sectors', [])

            # Load the JSON file
            current_directory = os.path.dirname(__file__)
            json_file_path = os.path.join(current_directory, 'permutation.json')

            with open(json_file_path, 'r') as file:
                companies = json.load(file)

            # Initialize data structures
            industries_data = {}
            sectors_data = {}
            total_companies = 0

            for company in companies:
                sector = company['Sector']
                industry = company['Industry']

                # Count companies per sector
                if sector in selected_sectors:
                    sectors_data[sector] = sectors_data.get(sector, 0) + 1

                    # Count companies per industry
                    industries_data[industry] = industries_data.get(industry, 0) + 1

                    total_companies += 1

            # Format data for ECharts
            industries_chart_data = [{"value": count, "name": industry} for industry, count in industries_data.items()]
            sectors_chart_data = [{"value": count, "name": sector} for sector, count in sectors_data.items()]

            return JsonResponse({
                "industries": industries_chart_data,
                "sectors": sectors_chart_data,
                "total_companies": total_companies
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except FileNotFoundError:
            return JsonResponse({'error': 'JSON file not found'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_industries_view(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            selected_industries = data.get('industries', [])

            # Load the JSON file
            current_directory = os.path.dirname(__file__)
            json_file_path = os.path.join(current_directory, 'permutation.json')

            with open(json_file_path, 'r') as file:
                companies = json.load(file)

            industries_data = []
            total_companies = 0
            for company in companies:
                if company.get('Industry') in selected_industries:
                    industries_data.append(company)
                    total_companies += 1

            # Structure the response data
            industries_chart_data = [
                {
                    "name": industry,
                    "value": sum(
                        company['Marketcap'] for company in industries_data if company['Industry'] == industry
                    )
                }
                for industry in selected_industries
            ]

            # Return the filtered data
            return JsonResponse({
                "industries": industries_chart_data,
                "total_companies": total_companies
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except FileNotFoundError:
            return JsonResponse({'error': 'JSON file not found'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def parse_range(range_value):
    """
    Parses a range string (e.g., '0-100', '100-500', '500+') into numerical start and end values.
    For '500+', the end is set to infinity.
    """
    if "+" in range_value:
        start = float(range_value.replace("+", ""))  # Remove '+' and convert to number
        end = float("inf")
    else:
        start, end = map(float, range_value.split("-"))  # Split by '-' and convert to numbers
    return start, end


def get_mvoh_metric_data_view(request):
    if request.method == 'POST':
        try:
            # Load the JSON file containing company data
            current_directory = os.path.dirname(__file__)
            json_file_path = os.path.join(current_directory, 'permutation.json')

            with open(json_file_path, 'r') as file:
                companies = json.load(file)

            # Parse request data
            data = json.loads(request.body)
            metric = data.get('metric')
            options = data.get('option', [])

            # Define scaling for specific metrics (e.g., billions)
            scale_factor = 1_000_000_000 if metric in ["MarketCap", "Operating_Cash_Flow"] else 1

            # Parse ranges and filter data
            filtered_companies = []
            for r in options:
                start, end = parse_range(r)  # Parse each range into numerical values
                start *= scale_factor
                end *= scale_factor
                for company in companies:
                    metric_value = company.get(metric, 0)
                    if start <= metric_value < end:
                        if company not in filtered_companies:
                            filtered_companies.append(company)

            # Prepare chart data
            chart_data = [{"name": c["Shortname"], "value": c[metric]} for c in filtered_companies]

            # Count number of companies
            company_count = len(filtered_companies)

            return JsonResponse({
                "chartData": chart_data,
                "companyCount": company_count
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def run_mvoh_model_view(request):

    context = {}

    return render(request, 'mvoh/summary_result.html', context)


def current_mvoh_result_view(request):

    context = {}

    return render(request, 'mvoh/run_output.html', context)


def output_view(request):
    context = {}

    return render(request, 'mvoh/run_output.html', context)