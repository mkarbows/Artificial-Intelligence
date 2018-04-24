from pomegranate import *

# You should use the Estimator module's CPTs for this purpose (fine to round parameters to 2 significant figures; they will be very close to clean values).
#
# First, determine who is currently charted to win the congressional seat and by what margin.
# Second, for each of the following, (a) compute the probability requested and then (b) determine whether or not the outreach team should target the individual for canvassing, and (c) record their values in your report.

# need to set inital vals of parents
ageGroup = DiscreteDistribution( { '0': 0.5, '1': 0.5 })
politicalLeaning = DiscreteDistribution( { '0': 0.5, '1': 0.5 } )

drugCPT = ConditionalProbabilityTable(
#     A, P, D, prob
    [[ '0', '0', '0', 0.45 ],
    [ '0', '0', '1', 0.55 ],
    [ '0', '1', '0', 0.75 ],
    [ '0', '1', '1', 0.25 ],
    [ '1', '0', '0', 0.3 ],
    [ '1', '0', '1', 0.7 ],
    [ '1', '1', '0', 0.15 ],
    [ '1', '1', '1', 0.85 ]], [ageGroup, politicalLeaning] )

gunControlCPT = ConditionalProbabilityTable(
#     A, G, prob
    [[ '0', '0', 0.3 ],
    [ '0', '1', 0.7 ],
    [ '1', '0', 0.6 ],
    [ '1', '1', 0.4 ]], [ageGroup] )

immigrationCPT = ConditionalProbabilityTable(
#     P, I, prob
    [[ '0', '0', 0.25 ],
    [ '0', '1', 0.75 ],
    [ '1', '0', 0.2 ],
    [ '1', '1', 0.8 ]], [politicalLeaning] )

votingCPT = ConditionalProbabilityTable(
#     I, G, V, prob
    [[ '0', '0', '0', 0.3 ],
    [ '0', '0', '1', 0.7 ],
    [ '0', '1', '0', 0.5 ],
    [ '0', '1', '1', 0.5 ],
    [ '1', '0', '0', 0.8 ],
    [ '1', '0', '1', 0.2 ],
    [ '1', '1', '0', 0.6 ],
    [ '1', '1', '1', 0.4 ]], [immigrationCPT, gunControlCPT] )

# # State objects hold both the distribution, and a high level name.
aState = State( ageGroup, name="ageGroup" )
pState = State( politicalLeaning, name="politicalLeaning" )
dState = State( drugCPT, name="drugCPT" )
gState = State( gunControlCPT, name="gunControlCPT" )
iState = State( immigrationCPT, name="immigrationCPT" )
vState = State( votingCPT, name="votingCPT" )

# # Create the Bayesian network object with a useful name
model = BayesianNetwork( "homework 4" )
#
# # Add the three states to the network
model.add_states(aState, pState, dState, gState, iState, vState)

# # Add transitions which represent conditional dependencies, where the second node is conditionally dependent on the first node (Monty is dependent on both guest and prize)
model.add_transition(aState, gState)
model.add_transition(aState, dState)
model.add_transition(gState, vState)
model.add_transition(iState, vState)
model.add_transition(pState, iState)
model.add_transition(pState, dState)

model.bake()

print(model.predict_proba({}))

# first task:
voting = model.predict_proba({})
print('voting')
print(voting[5].parameters[0])

# second task:
# add these to the report:
print('#1')                 # P(V | A=1)
print(model.predict_proba({'ageGroup':'1'}))
print('#2')
print(model.predict_proba({'gunControlCPT':'0'}))
print('#3')
print(model.predict_proba({'gunControlCPT':'0', 'immigrationCPT': '0'}))
print('#4')
print(model.predict_proba({'gunControlCPT':'1', 'immigrationCPT': '0'}))
print('#5')
print(model.predict_proba({'gunControlCPT':'0', 'immigrationCPT': '0', 'drugCPT':'0', 'politicalLeaning':'1', 'ageGroup':'0'}))
print('#6')
print(model.predict_proba({'gunControlCPT':'0', 'immigrationCPT': '1', 'drugCPT':'1', 'politicalLeaning':'1', 'ageGroup':'0'}))
print('#7')
print(model.predict_proba({'gunControlCPT':'1', 'immigrationCPT': '0', 'drugCPT':'0', 'politicalLeaning':'0', 'ageGroup':'1'}))
