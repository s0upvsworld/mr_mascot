from app.utils import Utilities as ut


def email_end(
    weekday,
    next_series_game_number,
    next_series_length,
    today_date,
    next_game_date,
    next_team,
):
    if next_series_game_number == 1:
        series_length = f"""
        It will be the first game in a {next_series_length} game series
        """
    else:
        series_length = f"""
        It will be game number {next_series_game_number} in the current {next_series_length} game series
        """
    if weekday == "Mon":
        standings = ut.nle()
        monday_nle_standings = f"""-In one sentence talk about the NLE standings the standings. If they are in first, get very excited. If they are last, remain hopeful. Reflect on what they need to do to win:\n\n{standings}\n\n
        """
    else:
        monday_nle_standings = " "
    
    end_prompt = f"""-Do not greet the reader again.\n\n
    {monday_nle_standings}
    -In one sentence notify the reader on the next game:
    --Today's Date: {today_date}.\n\n
    --Next Game Info: {next_game_date} against the {next_team}. {series_length}.\n\n
    --Only mention the series length if it's a new team or if it's the last game in the series.\n\n 
    --Do not say the year, and if the game is tonight, only say that.\n\n
    -Then in one sentence wish Friend well and say \'Let\'s Go Mets!\' and something endearing. Sign the end.
    """
    return end_prompt
