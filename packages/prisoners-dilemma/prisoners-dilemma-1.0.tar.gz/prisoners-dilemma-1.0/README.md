<a id="prisoners_dilemma"></a>

# prisoners\_dilemma

# Quick Start

The Prisoner's Dilemma is a game between two players. The players may choose to "cooperate" or "defect." Both players cooperations grants both players 2 points. Both players defection grants no points. If one player defect while the other cooperates, the defector gets 3 points and the cooperator gets -1 points.

This package can be used to run a simulation using the concept of the prisoner's dilemma.

This package is designed to be accessed from the command line using one of 
three commands:

```
dilemma-tournament
dilemma-population
dilemma-credits
```

dilemma-tournaments and -population have several additional arguments which can be given to modify the respective simulation. For more details on possible arguments see the following entries: prisoners-dilemma.tournament.tournament.tournament, prisoner-dilemma.population.population.population.

dilemma-tournament will run a series of dilemmas to test every included decision making algorithm against every other included algorithm. 

dilemma-population asigns "players" on a grid field decision-making algorithms. Then, it tests every player against their neighbors, identifies the lowest scorers, and asigns those lowest scorers a new decision-making algorithm. Thus, evolving the field until an end condition is met.

dilemma-credits simply prints urls pointing to the inspritation for this package.

If you want to include decision-making algorithms of your own, build python functions which take a single list of lists and return a boolean where True indicate cooperation. Place those python functions in one script and add "players=MYPLAYERS.py" to the end of your command line entry. The list of lists your bot must take in conatains data from your opponents previous decisions in the form:

[[opponent_name(str), opponent_first_decision(bool), opponent_first_points(int)],[opponent_name(str), opponent_second_decision(bool), opponent_second_points(int)]...]

If you must remember your previous decisions, this can be determined using the opponents previous decision and matched point values.

<a id="prisoners_dilemma.bots"></a>

## prisoners\_dilemma.bots

<a id="prisoners_dilemma.bots.bots"></a>

## prisoners\_dilemma.bots.bots

<a id="prisoners_dilemma.bots.bots.tit_for_tat"></a>

#### tit\_for\_tat

```python
def tit_for_tat(opponent_moves)
```

Player that copies opponents last move.

	Parameters
	----------
	opponent_moves: nested list structure
		Player algorithm.

<a id="prisoners_dilemma.bots.bots.always_defect"></a>

#### always\_defect

```python
def always_defect(opponent_moves)
```

Player always defects.

    Parameters
    ----------
    opponent_moves: nested list structure
        Player algorithm.

<a id="prisoners_dilemma.bots.bots.always_cooperate"></a>

#### always\_cooperate

```python
def always_cooperate(opponent_moves)
```

    Player always cooperates.

    Parameters
    ----------
    opponent_moves: nested list structure
        Player algorithm.

<a id="prisoners_dilemma.bots.bots.tester"></a>

#### tester

```python
def tester(opponent_moves)
```

Player first plays defect. If the opponent plays cooperate, tester will 
apologize by playing cooperate twice. After apologizing, or if the opponent
opens with defect, tester will play tit-for-tat.

    Parameters
    ----------
    opponent_moves: nested list structure
        Player algorithm.

<a id="prisoners_dilemma.bots.bots.grudge"></a>

#### grudge

```python
def grudge(opponent_moves)
```

Player cooperates until the opponent defects. Once the opponent defects,
player always defect.

    Parameters
    ----------
    opponent_moves: nested list structure
        Player algorithm.

<a id="prisoners_dilemma.bots.bots.random"></a>

#### random

```python
def random(_)
```

Player chooses randomly to cooperate or defect. Ignores input.

<a id="prisoners_dilemma.bots.bots.weighted_guess"></a>

#### weighted\_guess

```python
def weighted_guess(opponent_moves)
```

Player first plays cooperate. Then, makes a semi-random choice to defect
or cooperate weighted by the number of opponent cooperations. Will
cooperate more often if the opponent cooperates more often.

    Parameters
    ----------
    opponent_moves: nested list structure
        Player algorithm.

<a id="prisoners_dilemma.tournament"></a>

## prisoners\_dilemma.tournament

<a id="prisoners_dilemma.tournament.tournament"></a>

## prisoners\_dilemma.tournament.tournament

<a id="prisoners_dilemma.tournament.tournament.import_user_bots"></a>

#### import\_user\_bots

```python
def import_user_bots(filename)
```

This function imports a users file full of player algorithms.

    Parameters
    ----------
    filename: str
        Name of the python script to be imported, not including .py extension.

<a id="prisoners_dilemma.tournament.tournament.define_players"></a>

#### define\_players

```python
def define_players(players)
```

Defines list_of_players using built-in bots, plus any algorithms provided
by the user.

    Parameters
    ----------
    players: str
        Name of python script defining player functions, not including .py
        extesion.

<a id="prisoners_dilemma.tournament.tournament.tournament"></a>

#### tournament

```python
def tournament()
```

Intended for command line usage. Parses sys.argv list into kwargs. Then,
runs full tournament simulation and print results and benchmarks in
command line. For possible kwargs, see dilemma_tournament class and its 
tournament() method.

<a id="prisoners_dilemma.tournament.tournament.credits"></a>

#### credits

```python
def credits()
```

This method is accessible from command line and provides credit to the 
inspiration for this python package.

### dilemma\_tournament Objects

<a id="prisoners_dilemma.tournament.tournament.dilemma_tournament"></a>

```python
class dilemma_tournament()
```

The Prisoner's Dilemma is a game between two players. The players may
choose to "cooperate" or "defect." Both players cooperations grants both
players 2 points. Both players defection grants no points. If one player
defect while the other cooperates, the defector gets 3 points and the
cooperator gets -1 points.

This class runs a series of prisoner's dilemmas. It defines all player
algorithms using built-in bots from the prisoners-dilemma/bots package
and using functions in a user-defined python script. It contains methods
used to award points for decisions, test two player algorithms against each
other and test all player algorithms against all other player algorithms.

    Parameters
    ----------
    players: str, optional
    Name of .py script containing algorithms the user wants included. Note:
    algorithms must take in 1 argument that is nested lists containing
    opponent information. Player algorithms must return a bool for which
    True indicates Cooperation.
    n_rounds: int, optional
    Number of rounds played between each player algorithm. By default, the
    number of rounds played are randomly selected from a gaussian with a
    mean of 200 and standard deviation of 10
    rng_seed: int, optional
    rng seed can be given for replicability. Note: this seed in not passed
    to player algorithms. Player algorithm behavior may prevent perfect
    replication. default: None

<a id="prisoners_dilemma.tournament.tournament.dilemma_tournament.award_points"></a>

#### award\_points

```python
def award_points(decision_1, decision_2)
```

Awards points for decisions on a single prisoner's dilemma. Decisions
will be evaluated as booleans where True indicates Cooperation.

    Parameters
    ----------
    decision_1: bool
        The first player's decisions.
    decision_2: bool
        The second player's decisions.

<a id="prisoners_dilemma.tournament.tournament.dilemma_tournament.matchup"></a>

#### matchup

```python
def matchup(bot_1, bot_2)
```

This method runs some number of rounds of the prisoners dilemma by 
calling the award_points method n times. This method records all match 
information to all_results instance attribute, and awards points to the
final_score instance attribute.

    Parameters
    ----------
    bot_1: function
        Player algorithm.
    bot_2: function
        Player algorithm.

<a id="prisoners_dilemma.tournament.tournament.dilemma_tournament.tournament"></a>

#### tournament

```python
def tournament(show_scores=True,
               return_all_results=False,
               return_scores=False)
```

This method tests every player algorithm against each other. Each
player algorithm will play one "match" with each other player algorithm
once. A "match" is defined as some number of consecutive rounds. At the
end, the final score as well as a few benchmarks as printed.

    Parameters
    ----------
    show_scores: bool
    Prints the final score after tournament is run. default: True
    return_all_results: bool
    Returns results of every single dilemma instead of self. Note: if
    True, does not return self and other methods cannot be chained.
    default: False
    return_scores: bool
    Returns final scores instead of self. Note: if True, does not
    return self and other methods cannot be chained. default: False


<a id="prisoners_dilemma.population"></a>

## prisoners\_dilemma.population

<a id="prisoners_dilemma.population.population"></a>

## prisoners\_dilemma.population.population

<a id="prisoners_dilemma.population.population.population_mode"></a>

<a id="prisoners_dilemma.population.population.population"></a>

#### population

```python
def population()
```

Intended for command line usage. Parses sys.argv list into kwargs. Then,
runs full population simulation and generates images and gif. For possible
kwargs, see population_mode class and its run() method.

### population\_mode Objects

```python
class population_mode(dilemma_tournament)
```

This class places players on a map with certain decision making algorithms.
Each round tests each player against only it's neighbors some number of
times. Then, the worst performers of the population randomly change
strategies/decision-making-algorithms. After some number of rounds or when
a predetermined amount of the population is using the same algorithm, the
simulation ends. After the simulation ends, the results are made into
images and those images are turned into a gif all in a folder named
dilemma-fields.

    Parameters
    ----------
    players: str, optional
    Name of .py script containing algorithms the user wants included. Note:
    algorithms must take in 1 argument that is nested lists containing
    opponent information. Player algorithms must return a bool for which
    True indicates Cooperation.
    n_rounds: int, optional
    Number of rounds played between each player algorithm. By default, the
    number of rounds played are randomly selected from a gaussian with a
    mean of 50 and standard deviation of 2
    evolutions: int, optional
    Maximum number of field evolutions before simulation stops. In case of
    oscilation, this will prevent the sim from continuing indefinitely.
    default: 100
    field_size: tuple of 2 ints, optional
    This determines the size of the field. default: (10, 10)
    rng_seed: int, optional
    rng seed can be given for replicability. Note: this seed in not passed
    to player algorithms. Player algorithm behavior may prevent perfect
    replication. default: None
    quantile: float between 0 and 1, optional
    How much of the map should be replaced each round. 0 would replace
    nobody, 0.01 would replace the lowest 1%, and 1 would replace
    everybody. default: 0.2
    win_condition: float between 0 and 1, optional
    How much of the map must be taken before declaring a victor.
    default: 0.5

<a id="prisoners_dilemma.population.population.population_mode.spawn"></a>

#### spawn

```python
def spawn()
```

This method intially populated the field. Every player/point is
assigned a random algorithm such that the field is filled and 
randomized to start.

<a id="prisoners_dilemma.population.population.population_mode.round"></a>

#### round

```python
def round()
```

Runs a single round. Iterates through every player on the field from 
right to left, top to bottom. Tests every player-algorithm against all
neighbors below and to their immediate right. This ensure all player-
algorithms are only tested against each neighbor once. After finishing
a point's interation, that point's score is normalized to the number of
neighbors it has. This prevents the edge and corner positions from
unfair disadvantage.

<a id="prisoners_dilemma.population.population.population_mode.matchup"></a>

#### matchup

```python
def matchup(bot_1, bot_2, bot_1_loc, bot_2_loc)
```

This method runs some number of rounds of the prisoners dilemma by 
gathering each players deicision to cooperate of defect then calling 
the award_points method (inherited from the tournament class) n times.
This method records all match information to the score_array instance 
attribute.

    Parameters
    ----------
    bot_1: function
        Player algorithm.
    bot_2: function
        Player algorithm.
    bot_1_loc: tuple
        tuple indexing bot_1's position on the field
    bot_2_loc: tuple
        tuple indexing bot_2's position on the field

<a id="prisoners_dilemma.population.population.population_mode.respawn"></a>

#### respawn

```python
def respawn()
```

This method changes those lowest scoring players on the field to a
random new algorithm. It sets a cutoff score at the given quantile.
Then replaces all players scoring below that mark. All changed players
will change to the same new algorithm.

While changing players' algorithms, this method stores the current
score and field state in the score cube and field cube respectivelly.
Lastly, this method clears the score_array.

<a id="prisoners_dilemma.population.population.population_mode.check_convergence"></a>

#### check\_convergence

```python
def check_convergence()
```

This method checks if the win_condition had been met by any algorithm.
If it has, this method set the convergence flag to True.

<a id="prisoners_dilemma.population.population.population_mode.generate_images"></a>

#### generate\_images

```python
def generate_images()
```

At the end of the simulation, this method iterates throught the field
cube and turns every field state into a unique image titled with which
step in the evolution is depicted and a colorbar to indicated which
algorithms are being shown. Images are saved in a folder named
dilemma-fields, overwriting and images previously saved in the folder.

<a id="prisoners_dilemma.population.population.population_mode.generate_gif"></a>

#### generate\_gif

```python
def generate_gif()
```

Calls the generate_images method to produce .png images from every
field state. Then, this method turns those .png images into a gif to
make trends and emergent behaviors more clear. gif is save in a folder
name dilemma-fields with the images. Overwrites any previously saved
gif in the folder. Filename: dilemma-field-evolution.gif

<a id="prisoners_dilemma.population.population.population_mode.run"></a>

#### run

```python
def run(return_field_cube=False, return_score_cube=False)
```

This method runs the population simulation to it's conclusion. This
conclustion is either after so many evolutions or after a convergence
occurs and a winner is declared. This method does not generate images
or gifs on its own. That method must be called afterwards.

    Parameters
    ----------
    return_field_cube: bool, optional
    Returns cube containing every field state instead of self. If
    return_score_cube is also True, both are returned. Note: does not
    return self and other methods cannot be chained.
    default: False
    return_score_cube: bool, optional
    Returns cube containing all score arrays instead of self. If
    return_field_cube is also True, both are returned. Note: does not
    return self and other methods cannot be chained.
    default: False







