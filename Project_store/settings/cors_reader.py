from dotenv import load_dotenv

from utils.environment import get_env_variable, parse_comma_sep_str_to_list

load_dotenv()

CORS_ALLOWED_ORIGINS = parse_comma_sep_str_to_list(
    get_env_variable('CORS_TRUSTED_ORIGINS')
)
