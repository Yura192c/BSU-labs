#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

void print(string msg)
{
    cout << msg << "\n";
}

struct transition
{
    char symbol;
    int newState;
};

struct state
{
    int id;
    map<char, transition *> transitions;
    bool isVisited;
};

int inLength;
int outLength;
int statesCount;

set<char> inAlphabet;
set<char> outAlphabet;

vector<state *> states;

void meely()
{
}

void devisitAll()
{
    for (int i = 0; i < statesCount; i++)
    {
        states[i]->isVisited = false;
    }
}

bool areAllVisited()
{
    for (int i = 0; i < statesCount; i++)
    {
        if (states[i]->isVisited == false)
            return false;
    }
    return true;
}

bool areAllStatesReachable(int fromState)
{
    stack<int> st;
    st.push(fromState);
    devisitAll();
    states[fromState]->isVisited = true;
    while (st.size() > 0)
    {
        state *s = states[st.top()];
        st.pop();
        for (char c : inAlphabet)
        {
            state *next = states[s->transitions[c]->newState];
            if (next->isVisited == false)
            {
                next->isVisited = true;
                st.push(next->id);
            }
        }
    }

    return areAllVisited();
}

int createAutomate()
{
    print("Type in alphabet lenghtes");
    cin >> inLength;
    print("Type out alphabet lenghtes");
    cin >> outLength;

    if (inLength <= 1 || outLength <= 1)
    {
        print("Length is not correct");
        return 0;
    }

    print("Type in alphabet unique letters");
    for (int i = 0; i < inLength; i++)
    {
        char c;
        cin >> c;
        inAlphabet.insert(c);
        if (inAlphabet.size() == i)
        {
            print("Letter " + to_string(c) + " is dublicated in in alphabet");
            return 0;
        }
    }

    print("Type out alphabet unique letters");
    for (int i = 0; i < outLength; i++)
    {
        char c;
        cin >> c;
        outAlphabet.insert(c);
        if (outAlphabet.size() == i)
        {
            print("Letter " + to_string(c) + " is dublicated in out alphabet");
            return 0;
        }
    }

    print("Type states count");
    cin >> statesCount;
    if (statesCount <= 1)
    {
        print("Length is not correct");
        return 0;
    }

    for (int i = 0; i < statesCount; i++)
    {
        state *s = new state();
        s->id = i;
        s->isVisited = false;
        states.push_back(s);
    }

    print("Type transitions in format: '{out letter} {new state}'");
    for (int i = 0; i < statesCount; i++)
    {
        for (char c : inAlphabet)
        {
            print("For state " + to_string(i) + " for input letter " + c);

            char outLetter;
            int newState;
            cin >> outLetter >> newState;

            if (newState >= statesCount || newState < 0)
            {
                print("State " + to_string(newState) + " is out of range");
                return 0;
            }

            if (outAlphabet.find(outLetter) == outAlphabet.end())
            {
                print("Out letter is not in out alphabet");
                return 0;
            }
            transition *t = new transition();
            t->newState = newState;
            t->symbol = outLetter;

            states[i]->transitions.insert(make_pair(c, t));
        }
    }

    if (!areAllStatesReachable(0))
    {
        print("Some states cant be reached from root");
        return 0;
    }
}

struct treeNode
{
    vector<vector<int> > *statesGroups;
    treeNode **nextNodes;
};

set<vector<vector<int> > > uniqueStates;

vector<vector<int> > sumV(vector<vector<int> > v1, vector<vector<int> > v2)
{
    v1.insert(v1.end(), v2.begin(), v2.end());
    return v1;
}

vector<string> words;
void getWords(string route, vector<vector<int> > prevState)
{
    vector<vector<int> > newState;
    char currChar = route[route.length() - 1];
    for (vector<int> group : prevState)
    {
        map<char, vector<int> > newGroups;
        set<char> outChars;
        for (int stateId : group)
        {
            state *state = states[stateId];
            transition *tr = state->transitions[currChar];
            if (!newGroups.count(tr->symbol))
                newGroups.insert(make_pair(tr->symbol, vector<int>()));
            newGroups[tr->symbol].push_back(tr->newState);
            outChars.insert(tr->symbol);
        }

        for (char c : outChars)
        {
            newState.push_back(newGroups[c]);
        }
    }

    for (vector<int> group : newState)
    {
        for (int i = 0;i<statesCount;i++)
        {
            if (count(group.begin(), group.end(), i) > 1)
                return;
        }
    }

    int oldUSt = uniqueStates.size();
    uniqueStates.insert(newState);
    if (oldUSt == uniqueStates.size())
        return;

    if (statesCount == newState.size())
    {
        words.push_back(route);
        return;
    }

    for (char c : inAlphabet)
    {
        getWords(route + string(1, c), newState);
    }
}

int main()
{
    createAutomate();
    treeNode *root = new treeNode();
    root->statesGroups = new vector<vector<int> >();
    root->statesGroups->push_back(vector<int>());
    for (int i = 0; i < statesCount; i++)
    {
        root->statesGroups->at(0).push_back(i);
    }

    uniqueStates.insert(*(root->statesGroups));

    for (char c : inAlphabet)
    {
        getWords(string(1, c), *(root->statesGroups));
    }

    print("Words");
    for (string word : words)
    {
        print(word);
    }

    return 0;
}